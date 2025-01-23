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

image_label = ttk.Label(root, text='PICTURE WILL GO HERE').grid(column=2, row=1)

#create buttons

button = ttk.Button(root, text='Upload picture', command=upload_picture).grid(column=1, row=2)
button = ttk.Button(root, text='Add watermark', command=add_watermark).grid(column=3, row=2)
button = ttk.Button(root, text='Save picture', command=save_new_image).grid(column=2, row=3)

#allows screen to show
root.mainloop()