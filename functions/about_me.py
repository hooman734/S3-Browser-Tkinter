from tkinter import Toplevel, Label, LEFT, W
from PIL import Image, ImageTk


def about_me():
    about_me_window = Toplevel()
    about_me_window.geometry("400x160")
    about_me_window.title("Hooman Hesamyan  -  Developer")
    load = Image.open("info/hooman.png")
    render = ImageTk.PhotoImage(load)
    img = Label(about_me_window, image=render)
    img.image = render
    img.place(x=250, y=0)
    message = Label(about_me_window, anchor=W, justify=LEFT, text="""
    .: Hooman Hesamyan :.


    Web: hooman.hesamian.com
    Tell: +37477281774
    GitHub: github.com/hooman734

    """).pack(anchor=W)
