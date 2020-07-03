from tkinter import Toplevel, Label, LEFT


def help_credential_file():
    help_window = Toplevel()
    help_window.title("S3 - Browser       Help - Using Credential")
    message = Label(help_window, justify=LEFT, text="""
    Please route a credential file contains credential keys 
    that is composed similar to this sample:

    ----------------------------- Start of the *.csv file: -----------------------------

    AWSAccessKeyId=AKIAJ7HOXXXX2J5KQ4ZQ
    AWSSecretKey=vIe2X1kXXXXXXXXfBXnQfCY+JeP/PIxiZlAuW9DC

    ------------------------------ End of the *.csv file: ------------------------------

    """)
    message.pack()
