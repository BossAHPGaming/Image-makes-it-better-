from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("THE ONE PEICE IS REAL")
root.geometry('400x300')

upload = Image.open("ONE PIECE IS REAL.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width= 300)
label.place(x=50, y=0)
label2 = Label(root, text="THE ONE PICE IS REAL")
label2.place(x=40, y=360)

root.mainloop()