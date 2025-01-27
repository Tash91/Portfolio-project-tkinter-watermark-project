from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Add watermark to image")

root.geometry("650x500")

#create canvas


#create a frame widget 
content= ttk.Frame(root, borderwidth=5, relief="raised")

image= Image.open("goran-eidens-6T7kfc3VitU-unsplash.jpg")

resized_image= image.resize((300,225))

img = ImageTk.PhotoImage(resized_image)

insert_picture=Label(root,image= img)

picture_with_watermark= Label(root,image= img, text='This picture is water marked', compound='center', fg="grey")

delete_warning = Label(root, text='Window will close in 4 seconds', font=("Courier", 15))


def upload_picture():
    insert_picture.grid(column=1, row=1)
    insert_picture.image = img

   
def add_watermark():
    insert_picture.after(1000, insert_picture.destroy())
    picture_with_watermark.grid(column=1, row=1)
    picture_with_watermark.image = img

def delete_image():
    delete_warning.grid(column=1, row=0)
    picture_with_watermark.after(1000, picture_with_watermark.destroy())
    root.after(4000,lambda:root.destroy())



#creating buttons

button = ttk.Button(root, text='Upload picture', command=upload_picture).grid(column=0, row=2)
button = ttk.Button(root, text='Add watermark', command=add_watermark).grid(column=1, row=2)
button = ttk.Button(root, text='Delete picture', command=delete_image).grid(column=2, row=2)

#allows screen to show
root.mainloop()