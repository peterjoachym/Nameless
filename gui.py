
import os
import tkinter as tk
from tkinter import ttk
from fileinput import FileInput
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from pdf_to_text import *
from Fonctions.hash import decrypt_filename

def open_file():
    file_path= askopenfile(mode='r', filetypes=[('All Files', '*.*')])
    if file_path is not None:
        pass
    print (file_path)

def open_folder():
    global origin_folder_path 
    origin_folder_path = filedialog.askdirectory(initialdir=os.path.normpath("..//"), title="Example")
    origin_folder['text']="Origin folder selected:"+origin_folder_path
    
def destination_folder():
    global destination_folder_path
    destination_folder_path = filedialog.askdirectory(initialdir=os.path.normpath("..//"), title="Example")
    dest_folder['text']="Destination folder selected:"+ destination_folder_path

def show_entry_fields():
    print("Identifier: %s" % (e1.get()))
    token_byte = e1.get()[1:].encode()
    original_filename['text']=(decrypt_filename(token_byte))




root = tk.Tk()
root.title("Nameless")
root.geometry('1000x600')
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)


tabControl.add(tab1, text ='Converter')
tabControl.add(tab2, text ='Identifier')

tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab1,
          text ="Convert your files").grid(column = 15,
                               row = 15,
                               padx = 20,
                               pady = 10)

ttk.Label(tab1,
          text ='Choose Files:').grid(column = 15,
                               row = 40,
                               padx = 10,
                               pady = 10)



ttk.Button(tab1,text='Open', command=lambda:open_folder(), width=15).grid(column = 16,
                               row = 40,
                               padx = 0,
                               pady = 10)

origin_folder=ttk.Label(tab1, text="", foreground= 'green')

origin_folder.grid(column = 16,
                   row = 42,
                   padx = 0,
                   pady = 10)

ttk.Label(tab1,
          text ='Destination Files:').grid(column = 15,
                               row = 50,
                               padx = 10,
                               pady = 10)

ttk.Button(tab1,text='Open', command=lambda:destination_folder(), width=15).grid(column = 16,
                     row = 50,
                     padx = 20,
                     pady=10)

dest_folder=ttk.Label(tab1, text=" ",  foreground='green')

dest_folder.grid(column = 16,
                     row = 55,
                     padx = 20,
                     pady= 30)

def convert_files(origin_folder, dest_folder):
    dir_path=origin_folder.get()
    dir_path_dest=dest_folder.get()
    print (dir_path, dir_path_dest)

ttk.Button(tab1,text='Convert', command=lambda:pdf_to_txt(origin_folder_path, destination_folder_path), width=15).grid(column = 16,
                        row = 56,
                        padx=20,
                        pady=10)

ttk.Label(tab2,
          text ="Find original file").grid(column = 0,
                                    row = 0,
                                    padx = 30,
                                    pady = 30)

ttk.Label(tab2, text="Identifier: ").grid(row=20, column=25)
e1 = tk.Entry(tab2)
e1.grid(row=20, column=30)

ttk.Button(tab2, text="Find", command=show_entry_fields).grid(column=40,
                                row=20,
                                padx=10)

original_filename=ttk.Label(tab2, text=" ",  foreground='green')

original_filename.grid(column = 30,
                     row=30,
                     padx = 0,
                     pady= 20)
ttk.Label(tab2)



root.mainloop()

#fucntions remaining to be coded, confirm, open multiple files, make look cleaner, change passsphrase
