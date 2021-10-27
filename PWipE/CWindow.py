from tkinter import *

from tkinter import filedialog , ttk

import os

class CWindow:

    def __init__(self, master):

        b_open_file = BooleanVar()
        b_open_folder = BooleanVar()

        content = ttk.Frame(master)

        frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=400, height=200)

        self.quit_button = Button(content, text="Quit", command=frame.quit)

        self.open_file_button = Button(content, text="Open", command=lambda:self.OpenFile(master))

        self.open_file_checkbox = ttk.Checkbutton(content, text="File", variable=b_open_file, onvalue=True)

        self.open_folder_checkbox = ttk.Checkbutton(content, text="Folder", variable=b_open_folder, onvalue=True)

        content.grid(column=0, row=0)

        self.quit_button.grid(column=3, row=3)

        self.open_file_button.grid(column=3,row=0)

        self.open_file_checkbox.grid(column=0, row=0)

        self.open_folder_checkbox.grid(column=0, row=3)

    def OpenFile(self,master):
        self.dirname = filedialog.askdirectory(parent=master,initialdir="/",title='Please select a directory')
        self.WipeFile(self.dirname)

    def WipeFile(self,name):
        self.dir = name
        os.system("wipe -r -f "+ self.dir)
