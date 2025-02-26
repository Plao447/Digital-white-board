from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os

root = Tk()
root.title("WHITE BOARD")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False, False)

current_x = 0
current_y = 0
color = 'black'

def locate_xy(work):
    global current_x, current_y

    current_x = work.x
    current_y = work.y

def add_line(work):
    global current_x, current_y
    canvas.create_line((current_x, current_y, work.x , work.y), width=get_current_value(),
                       fill= color, capstyle=ROUND, smooth=True)

    current_x ,current_y = work.x, work.y

def show_color(new_color):
    global color

    color = new_color

def new_canvas():
    canvas.delete('all')
    display_palette()

def insert_image():
    global filename
    global f_img

    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetypes=(("PNG file", "*.png"),("All files", "*.*")))

    f_img = tk.PhotoImage(file=filename)
    canvas.create_image(180, 50, image=f_img)
    root.bind("<B3-Motion>", my_callback)

def my_callback(event):
    global f_img
    f_img = tk.PhotoImage(file=filename)
    canvas.create_image(event.x, event.y, image=f_img)

#---------------------------------------------

#ICON

image_icon = PhotoImage(file="image/logo.png")
root.iconphoto(False, image_icon)

#----------------------------------------------

#SIDER

color_box = PhotoImage(file="image/color section.png")
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)

eraser = PhotoImage(file="image/eraser.png")
Button(root, image=eraser, bg="#f2f3f5", command=new_canvas).place(x=30, y=400)

import_image = PhotoImage(file="image/add_image.png")
Button(root, image=import_image, bg="white", command=insert_image).place(x=30, y=450)

#------------------------------------------------

#COLOR

colors = Canvas(root, bg="#fff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_palette():
    Id = colors.create_rectangle((10, 10, 30, 30), fill="black")
    colors.tag_bind(Id, '<Button-1>', lambda x: show_color('black'))

    Id = colors.create_rectangle((10, 40, 30, 60), fill="gray")
    colors.tag_bind(Id, '<Button-1>', lambda x: show_color('gray'))

    Id = colors.create_rectangle((10, 70, 30, 90), fill="brown")
    colors.tag_bind(Id, '<Button-1>', lambda x: show_color('brown'))

    Id = colors.create_rectangle((10, 100, 30, 120), fill="red")
    colors.tag_bind(Id, '<Button-1>', lambda x: show_color('red'))

    Id = colors.create_rectangle((10, 130, 30, 150), fill="orange")
    colors.tag_bind(Id, '<Button-1>', lambda x: show_color('orange'))

    Id = colors.create_rectangle((10, 160, 30, 180), fill="yellow")
    colors.tag_bind(Id, '<Button-1>', lambda x: show_color('yellow'))

    Id = colors.create_rectangle((10, 190, 30, 210), fill="green")
    colors.tag_bind(Id, '<Button-1>', lambda x: show_color('green'))

    Id = colors.create_rectangle((10, 220, 30, 240), fill="blue")
    colors.tag_bind(Id, '<Button-1>', lambda x: show_color('blue'))

    Id = colors.create_rectangle((10, 250, 30, 270), fill="purple")
    colors.tag_bind(Id, '<Button-1>', lambda x: show_color('purple'))

display_palette()

#-------------------------------------------------

#MAIN-SCREEN

canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', add_line)

#-------------------------------------------------

#SLIDER
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

#--------------------------------------------------


mainloop()
