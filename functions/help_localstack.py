from tkinter import Toplevel, Label, W, LEFT


def help_localstack():
    help_window = Toplevel()
    help_window.title("S3 - Browser       Help - Localstack")
    help_window.geometry("500x200")
    message = Label(help_window, anchor=W, justify=LEFT, text="""
    To use localstack fake S3 service, the only thing you need to do is 
    inserting your custom endpoint url.

    But make sure that beforehand, you logged in with either a credential 
    csv file or directly adding Access key Id and Secret key.


    *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
    *   Tip: In case of using Localstack, there is no need to insert valid                            
    *    Access key Id and Secret key. (It is not going to be authenticated!)                                  
    *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   * 
    """)
    message.pack()
