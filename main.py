from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Add watermark to image")

root.geometry("500x500")

#create canvas


#create a frame widget 
content= ttk.Frame(root, borderwidth=5, relief="raised")

image= Image.open("goran-eidens-6T7kfc3VitU-unsplash.jpg")

resized_image= image.resize((300,225))

img = ImageTk.PhotoImage(resized_image)

insert_picture=Label(root,image= img)

picture_with_watermark= Label(root,image= img, text='This picture is water marked', compound='center', fg="grey")

def upload_picture():
    insert_picture.grid(column=1, row=1)
    insert_picture.image = img

   
def add_watermark():
    picture_with_watermark.grid(column=1, row=1)
    picture_with_watermark.image = img

def delete_image():
    picture_with_watermark.after(1000, picture_with_watermark.destroy())



#creating buttons

button = ttk.Button(root, text='Upload picture', command=upload_picture).grid(column=0, row=1)
button = ttk.Button(root, text='Add watermark', command=add_watermark).grid(column=0, row=2)
button = ttk.Button(root, text='Delete picture', command=delete_image).grid(column=0, row=3)

#allows screen to show
root.mainloop()