# S3-Browser
# Implemented by Hooman Hesamyan
# Using Tkinter


# import all necessary modules and error handlers from the library
from tkinter import *
from tkinter import filedialog
import botocore.exceptions as exc
import boto3

# import custom module to extract credential keys
from functions.User_credential import get_keys
from functions.help_credential_file import help_credential_file
from functions.help_localstack import help_localstack
from functions.about_me import about_me
from functions.animating_bar import show_progress

# initiate main window
root = Tk()
root.title("S3-Browser    By Hooman Hesamyan V2.0")

# initiate parameters
t = ''
user_access_key_id = ''
key_id = StringVar()
user_secret_access_key = ''
access_key = StringVar()
user_endpoint_url = StringVar()
user_endpoint_url.set("http://localhost:4572/")
s3 = ''
s3_client = ''
is_local = BooleanVar(False)
counter = 1
state = {"login": NORMAL,
         "browser": DISABLED}


# function for initiating boto3 instances
def init_services():
    global s3
    global s3_client
    if is_local.get():  # in case of having custom end-point
        try:
            s3_client = boto3.client('s3',
                                     endpoint_url=user_endpoint_url.get(),
                                     aws_access_key_id=user_access_key_id,
                                     aws_secret_access_key=user_secret_access_key
                                     )
            s3 = boto3.resource('s3',
                                endpoint_url=user_endpoint_url.get(),
                                aws_access_key_id=user_access_key_id,
                                aws_secret_access_key=user_secret_access_key
                                )
        except exc.NoCredentialsError:
            aws_status_label['text'] = "Failed to login!"
            aws_status_label['bg'] = 'red'
            aws_status_label['fg'] = 'Yellow'
        except Exception:
            aws_status_label['text'] = "Failed to login!"
            aws_status_label['bg'] = 'red'
            aws_status_label['fg'] = 'Yellow'

    else:  # in case of using AWS url
        try:
            s3_client = boto3.client('s3',
                                     aws_access_key_id=user_access_key_id,
                                     aws_secret_access_key=user_secret_access_key
                                     )
            s3 = boto3.resource('s3',
                                aws_access_key_id=user_access_key_id,
                                aws_secret_access_key=user_secret_access_key
                                )
        except exc.NoCredentialsError:
            aws_status_label['text'] = "Failed to login!"
            aws_status_label['bg'] = 'red'
            aws_status_label['fg'] = 'Yellow'
        except exc.EndpointConnectionError as e:
            aws_status_label['text'] = "Failed to login!"
            aws_status_label['bg'] = 'red'
            aws_status_label['fg'] = 'Yellow'
            print("--------->", e)


# function for managing entry fields, and proceeding login procedure by starting boto3
def login():
    global user_access_key_id
    global user_secret_access_key
    global s3
    global s3_client
    global state

    user_access_key_id = aws_key_id_entry.get()
    user_secret_access_key = aws_secret_access_key_entry.get()
    global counter
    if len(user_access_key_id) == 0 or len(user_secret_access_key) == 0:
        aws_login_key.flash()
        aws_login_key['text'] = "Login - retry {}".format(counter)
        counter += 1

    else:
        init_services()
        aws_key_id_entry.delete(0, END)
        aws_secret_access_key_entry.delete(0, END)
        aws_browser_button['state'] = NORMAL
        aws_status_label['text'] = "Credential imported"
        aws_status_label['bg'] = '#61099c'
        aws_status_label['fg'] = 'Yellow'
        aws_browser_button.pack()


# function for using *.csv and proceeding on the main window

def open_csv():
    global user_access_key_id
    global user_secret_access_key

    root.filename = filedialog.askopenfilename(initialdir="~/Downloads",
                                               title="Select key.csv file",
                                               filetypes=(("csv files", "*.csv"), ("txt files", "*.txt")))

    aws_get_key_label['text'] = ''
    aws_get_key_label2 = Label(aws_login_with_csv, text="Extracted keys using:" + root.filename.split('/')[-1])
    aws_get_key_label2.grid(row=3, column=2, columnspan=6)
    user_access_key_id, user_secret_access_key = get_keys(root.filename)
    global key_id
    key_id.set(user_access_key_id)
    global access_key
    access_key.set(user_secret_access_key)
    aws_browser_button.pack()


# function for reading and demonstrating all buckets' names
def iterate_over_buckets():
    buckets = Toplevel()
    buckets.title("Buckets")
    bucket_label = LabelFrame(buckets, text="All buckets are:")
    list_box = Listbox(bucket_label, bg="#e8ae95", selectmode=SINGLE, width=50, selectbackground="#bf06b9", cursor="")
    list_box.activate(END)
    action_box = LabelFrame(buckets, text="Choose action:")

    # animating a bar to show that process is ongoing
    show_progress(root)

    i = 1
    try:
        for bucket in s3.buckets.all():
            list_box.insert(i, bucket.name)
            i += 1

        state["is-connected"] = True
        list_box.pack()
        bucket_label.pack()

        download_button = Button(action_box, text="Open!", padx=50,
                                 command=lambda: iterate_over_files(
                                     list_box.get(0) if len(list_box.curselection()) == 0 else list_box.get(
                                         list_box.curselection())))
        upload_button = Button(action_box, text="Upload!", padx=50,
                               command=lambda: upload_file(
                                   list_box.get(0) if len(list_box.curselection()) == 0 else list_box.get(
                                       list_box.curselection())))
        download_button.grid(row=0, column=0)
        upload_button.grid(row=0, column=1)
        action_box.pack()
        aws_status_label['text'] = "Logged in Successfully!"
        aws_status_label['bg'] = 'Green'
        aws_status_label['fg'] = 'Yellow'

    except exc.EndpointConnectionError as e:
        aws_status_label['text'] = "Login failed!"
        aws_status_label['fg'] = 'yellow'
        aws_status_label['bg'] = '#781e00'
        list_box.insert(i, str(e).split(':')[0] + ' : ')
        list_box.insert(i + 1, '"https://' + str(e).split('//')[-1])
        print("--------->", e)

        list_box.pack()
        bucket_label.pack()

        exit_button = Button(action_box, text="Exit!", padx=100, command=lambda: buckets.quit())

        exit_button.grid(row=0, column=0, columnspan=2)

        action_box.pack()


# function for reading and demonstrating all files' names inside a selected bucket
def iterate_over_files(aws_bucket_name):
    if len(aws_bucket_name) == 0:
        return
    files = Toplevel()
    files.title("Files")
    files_label = LabelFrame(files, text="All files are:")
    Label(files_label, text="Inside bucket: " + aws_bucket_name, fg="#b82c06").pack()
    succeed_response = Label(files_label, justify=LEFT, anchor=W, text="""
    Info!
    Download succeed.
    (Saved in the main directory)
    """, fg="#b82c06")
    failed_response = Label(files_label, text="Download failed", fg="#b82c06")
    list_box = Listbox(files_label, bg="#abe895", selectmode=SINGLE, width=50, selectbackground="#19bf06")

    for file in s3.Bucket(aws_bucket_name).objects.all():
        i = 1
        list_box.insert(i, file.key)
        i += 1
    list_box.pack()
    files_label.pack()
    select_button = Button(files_label, text="Download file!", padx=50,
                           command=lambda: download_file(aws_bucket_name, list_box.get(list_box.curselection()),
                                                         succeed_response, failed_response))
    select_button.pack()


# function for downloading a selected file
# to download, using boto3 instance
def download_file(aws_bucket_name, aws_object_name, okay, fail):
    file_name = str(aws_object_name)[:].split('/')[-1]
    try:
        s3_client.download_file(aws_bucket_name, aws_object_name, file_name)
        okay.pack()
        # CP(file_name, '~/Desktop')
        print("Download was successful")

    except exc.ClientError:
        fail.pack()
        print("")


# function for uploading a selected file
def upload_file(aws_bucket_name):
    upload_files = Toplevel()
    upload_files.title("Files")
    files_label = LabelFrame(upload_files, text="Upload a file:")
    upload_key_label = LabelFrame(upload_files)
    Label(files_label, text="Selected bucket: " + aws_bucket_name, fg="#b82c06").pack()
    Label(upload_key_label, text="Choose a name for uploading file: ").grid(row=0, column=0)
    selected_name_file = Entry(upload_key_label)
    succeed_response = Label(files_label, text="Uploading succeed!")
    failed_response = Label(files_label, text="Uploading failed!")
    selected_name_file.grid(row=0, column=1)
    Button(upload_key_label, text="Upload selected file",
           command=lambda: upload(root.filename, aws_bucket_name, selected_name_file.get())).grid(row=2, column=0,
                                                                                                  columnspan=2)

    files_label.pack()
    upload_key_label.pack()

    root.filename = filedialog.askopenfilename(initialdir="~/Pictures",
                                               title="Select a file to upload",
                                               filetypes=(("all files", "*.*"),
                                                          ("image files",
                                                           ("*.jpg", "*.jpeg", "*.png")),
                                                          ("document files",
                                                           ("*.doc", "*.docs", "*.odt", "*.pdf", "*.txt"))))

    Label(files_label, text="Selected file: " + root.filename.split('/')[-1], fg="#b82c06").pack()

    # to upload, using boto3 instance
    def upload(local_file, bucket_name, s3_file):
        try:
            s3_client.upload_file(local_file, bucket_name, s3_file if len(s3_file) != 0 else local_file.split('/')[-1])
            succeed_response.pack()
            print("Upload Succeed")

        except FileNotFoundError:
            failed_response.pack()
            print("failed to upload...")


# Defining the menu bar
app_menu = Menu(root)
root.config(menu=app_menu)

# Defining the menu bar sub elements and their functionality
info_Menu = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="Information", menu=info_Menu)
help_Menu = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="Help", menu=help_Menu)

info_Menu.add_command(label="About Developer", command=lambda: about_me())
info_Menu.add_separator()
info_Menu.add_command(label="Exit!", command=lambda: root.quit())

help_Menu.add_command(label="CSV credential", command=lambda: help_credential_file())
help_Menu.add_separator()
help_Menu.add_command(label="Localstack", command=lambda: help_localstack())

# Defining elements
introduction = Label(root, text="For using S3-browser please insert these information:", fg="#69054b",
                     font=("Arial", 16),
                     justify=LEFT,
                     padx=200, relief=SUNKEN, bd=1)
aws_status_bar = LabelFrame(root, text='')
aws_login_with_keys = LabelFrame(root, text="Setup Credential", pady=10)
aws_login_with_csv = LabelFrame(root, text="Read CSV file", pady=30)
aws_browse_content = LabelFrame(root, text="Browser...")

aws_status_label = Label(aws_status_bar, state=DISABLED, bg='blue', text="Not logged in...", fg='white',
                         font=("Verdana", 10))
aws_key_id_label = Label(aws_login_with_keys, text="Access Key Id: ", fg="#052b69", anchor=E, relief=SUNKEN, bd=1,
                         padx=50)
aws_secret_access_key_label = Label(aws_login_with_keys, text="Secret Key: ", fg="#052b69", anchor=E, relief=SUNKEN,
                                    bd=1, padx=50)
aws_endpoint_address_label = Label(aws_login_with_keys, text="End-point address: ", fg="#052b69", anchor=E,
                                   relief=SUNKEN,
                                   bd=1, padx=50)
aws_endpoint_checkbox = Checkbutton(aws_login_with_keys, text="use", variable=is_local)
aws_get_key_label = Label(aws_login_with_csv, anchor=W, justify=LEFT, text="""
* Input credential either manually or by importing
*  from CSV file then hit the  "Import Credential!"
* button.""")

aws_key_id_entry = Entry(aws_login_with_keys, textvariable=key_id)
aws_secret_access_key_entry = Entry(aws_login_with_keys, textvariable=access_key, show='*')
aws_endpoint_address_entry = Entry(aws_login_with_keys, textvariable=user_endpoint_url)

# Main window credential id and key buttons
aws_login_key = Button(aws_login_with_keys, text="Import Credential!", padx=50, command=lambda: login(), fg="#052b69",
                       borderwidth="2", state=state['login'])
aws_get_key_file = Button(aws_login_with_csv, text="Choose Credential File...", command=lambda: open_csv(),
                          fg="#052b69", borderwidth="2", padx=50)
aws_browser_button = Button(aws_browse_content, text="Login and Browse Buckets...",
                            command=lambda: iterate_over_buckets(), state=state['browser'], padx=100)

# Setting the layout of the main window
# Main elements
introduction.grid(row=0, column=0, columnspan=6)
aws_status_bar.grid(row=1, column=0, columnspan=6, sticky=E)
aws_login_with_keys.grid(row=2, column=1)
aws_login_with_csv.grid(row=2, column=2)
aws_browse_content.grid(row=3, column=1, columnspan=2)

# Secondary elements
aws_key_id_label.grid(row=1, column=0, sticky=W + E)
aws_secret_access_key_label.grid(row=2, column=0, sticky=W + E)
aws_key_id_entry.grid(row=1, column=1)
aws_secret_access_key_entry.grid(row=2, column=1)
aws_endpoint_address_label.grid(row=3, column=0)
aws_endpoint_address_entry.grid(row=3, column=1)
aws_login_key.grid(row=4, column=0, columnspan=2)
aws_get_key_file.grid(row=1, column=2, columnspan=3)
aws_get_key_label.grid(row=2, column=2, columnspan=3)
aws_endpoint_checkbox.grid(row=3, column=2)
aws_status_label.pack()

# Main window loop
root.mainloop()
