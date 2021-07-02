# Importing libraries - tkinter for GUI, Pillow/PIL for image processing and showing, random module for choosing random image of a list

import tkinter as tk
from PIL import ImageTk, Image
import random

# Defining our main window, naming it and resizing it as fixed width and height depending on size of image
window = tk.Tk()
window.title("Image Processing")
window.resizable(0, 0)

# defining Frame for image
imgFrame = tk.Frame(master=window, bd=2, width=50)
imgFrame.pack(side=tk.LEFT)

# Getting a list of image, choosing a random image to display and then displaying it using PIL module inside Label widget

images = ['baboon.jpg', 'apple.jpg', 'board.jpg', 'fruits.jpg', 'orange.jpg', 'WindowsLogo.jpg', 'starry_night.jpg', 'cards.png', 'graf1.png', 'ml.png', 'opencv-logo.png', 'opencv-logo-white.png', 'pic2.png', 'smarties.png', ]
imgchoose = random.choice(images)
imglink = "images//" + str(imgchoose)

img = Image.open(imglink)
my_image = ImageTk.PhotoImage(img)

label = tk.Label(master=imgFrame, image=my_image)
label.grid(padx=20, pady=20)

# Function used in the "Refresh" button to show the changing image
def refresh_image():
    images = ['baboon.jpg', 'apple.jpg', 'board.jpg', 'fruits.jpg', 'orange.jpg', 'WindowsLogo.jpg', 'starry_night.jpg', 'cards.png', 'graf1.png', 'ml.png', 'opencv-logo.png', 'opencv-logo-white.png', 'pic2.png', 'smarties.png', ]
    imgchoose = random.choice(images)
    imglink = "images//" + str(imgchoose)
    global img
    img = Image.open(imglink)
    img2 = ImageTk.PhotoImage(img)
    label.configure(image=img2)
    label.image = img2

# Defining Frame for buttons

controlFrame = tk.Frame(master=window, bg="black", bd=0, width=30)
controlFrame.pack(side=tk.RIGHT, padx=20, pady=20)

# Function used in the "Red", "Green", "Blue" button to show the R/G/B colored image respectively
def show_img(ind):
    img2 = Image.Image.split(img)
    if ind==0:
        img2 = ImageTk.PhotoImage(img2[0])
    elif ind==1:
        img2 = ImageTk.PhotoImage(img2[1])
    elif ind==2:
        img2 = ImageTk.PhotoImage(img2[2])
    label.configure(image=img2)
    label.image = img2

# Function used in the "Colored" button to show the original colored image
def show_colored():
    img2 = ImageTk.PhotoImage(img)
    label.configure(image=img2)
    label.image = img2

# defining buttons used for control and displaying it using grid in earlier defined frame for buttons
# Button with text Red show image R of RGB image, Green button shows image G of RGB image, Blue shows B of RGB image, Colored button shows original image, Refresh shows any other image using random module and it has all the options available to it.
# Exit button exits the program and loops out of window.

btn1 = tk.Button(master=controlFrame, text="Red", width=20, padx=5, pady=5, command=lambda: show_img(0), activebackground="yellow").grid(row=0, padx=10, pady=10)
btn2 = tk.Button(master=controlFrame, text="Green", width=20, padx=5, pady=5, command=lambda: show_img(1), activebackground="yellow").grid(row=1, padx=10, pady=5)
btn3 = tk.Button(master=controlFrame, text="Blue", width=20, padx=5, pady=5, command=lambda: show_img(2), activebackground="yellow").grid(row=2, padx=10, pady=5)
btn4 = tk.Button(master=controlFrame, text="Colored", width=20, padx=5, pady=5, command=show_colored, activebackground="yellow").grid(row=3, padx=10, pady=5)
btn5 = tk.Button(master=controlFrame, text="Refresh", width=20, padx=5, pady=5, command=refresh_image, activebackground="yellow").grid(row=4, padx=10, pady=5)
btn6 = tk.Button(master=controlFrame, text="Exit", width=20, padx=5, pady=5, command=window.quit, activebackground="yellow").grid(row=5, padx=10, pady=10)

# executing mainloop() that traces the activities inside window and run the program
window.mainloop()