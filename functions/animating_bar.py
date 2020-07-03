import time
from tkinter import HORIZONTAL, W, E
from tkinter.ttk import Progressbar


def show_progress(root):
    # Progress bar widget
    progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')

    # Function responsible for the updating
    # of the progress bar value
    progress.grid(row=5, column=1, columnspan=3, sticky=W+E)

    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
