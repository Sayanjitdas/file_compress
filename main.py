import tkinter as tk
from tkinter import filedialog
from compress import compress_file

def open_file():
    file_name = filedialog.askopenfilename(initialdir="./",title="Select a file")
    return file_name

def show_file():
    file_name = open_file()
    show_file.config(text=file_name)

def compress(filepath):
    
    out_file = compress_file(filepath)
    show_out_file.config(text=out_file)

root = tk.Tk()


# setting the root window geometry
root.geometry("600x400")

# adding title
root.title("Compressor")

# file name
select_file_btn = tk.Button(root,text="Select file..",command=show_file)
select_file_btn.grid(row=0,column=0)

# label to show file_name to be compressed
show_file = tk.Label(root)
show_file.grid(row=0,column=1,padx=2)


# compress btn
compress_btn = tk.Button(root,text="Compress",command=lambda:compress(show_file.cget('text')))
compress_btn.grid(row=1,column=0,pady=4)

# output label
show_out_file = tk.Label(root)
show_out_file.grid(row=1,column=1,padx=2)

root.mainloop()