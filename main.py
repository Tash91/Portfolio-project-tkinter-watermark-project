from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Add watermark to image")

def upload_picture():
    pass

def add_watermark():
    pass

def save_new_image():
    pass

#create a frame widget 
frame = ttk.Frame(root, borderwidth=5, relief="raised")

#create labels

upload_image_label = ttk.Label(root, text='Click here to upload image').grid(column=1, row=2)
upload_watermark_label = ttk.Label(root, text='Click here to upload watermark').grid(column=3, row=2)
save_label = ttk.Label(root, text='Click here to save').grid(column=2, row=3)

#create buttons

button = ttk.Button(root, text='Okay', command=upload_picture)
button = ttk.Button(root, text='Okay', command=add_watermark)
button = ttk.Button(root, text='Okay', command=save_new_image)

#allows screen to show
root.mainloop()