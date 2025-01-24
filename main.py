from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Add watermark to image")

root.geometry("500x500")

#create canvas



def add_watermark():
    pass

def save_new_image():
    pass

#create a frame widget 
content= ttk.Frame(root, borderwidth=5, relief="raised")

def upload_picture():
    image= Image.open("goran-eidens-6T7kfc3VitU-unsplash.jpg")

    resized_image= image.resize((300,225))

    img = ImageTk.PhotoImage(resized_image)

    Label(root,image= img).grid(column=1, row=1)

    Label.image = img


#create image

# image= Image.open("goran-eidens-6T7kfc3VitU-unsplash.jpg")

# resized_image= image.resize((300,225))

# img = ImageTk.PhotoImage(resized_image)

# Label(root,image= img).grid(column=1, row=1)


#creating buttons

button = ttk.Button(root, text='Upload picture', command=upload_picture).grid(column=0, row=1)
button = ttk.Button(root, text='Add watermark', command=add_watermark).grid(column=0, row=2)
button = ttk.Button(root, text='Save picture', command=save_new_image).grid(column=0, row=3)

#allows screen to show
root.mainloop()