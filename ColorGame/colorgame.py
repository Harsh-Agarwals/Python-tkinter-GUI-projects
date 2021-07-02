# Importing tkinter library for GUI and random module for choosing random index of the list
import tkinter as tk
import random

# Defining and renaming window
window = tk.Tk()
window.title("Color GAME")

# Colors and words, which will be used to select the text to be displayed and color over it
colors = ["red", "yellow", "green", "pink", "white", "blue", "orange", "purple", "brown", "black"]
words = ["Red", "Yellow", "Green", "Pink", "White", "Blue", "Orange", "Purple", "Brown", "Black"]

# First label, ABOUT GAME
heading = tk.Label(window, text="Type in the color of the words and not the word text!", font='ariel 11 bold')
heading.pack(padx=5, pady=5)

# Second label, ABOUT TIME GIVEN
start = tk.Label(window, text="Score maximum in 30 seconds")
start.pack()

# Label 3rd, displaying score
score = 0
scr = tk.Label(window, text="Score: " + str(score))
scr.pack()

# Label 4th, displaying real time left
lefttime = 30
timelabel = tk.Label(window, text="Time left: "+str(lefttime))
timelabel.pack()

# Choosing random color and word using random.choice module
color = random.choice(colors)
word = random.choice(words)

# Label displaying chosen word colored with the chosen color
maintext = tk.Label(window, text=word, fg=color, font='Helvetica 20 bold')
maintext.pack()

# Game over function
def gameover():
    window.destroy()

# Function displaying realtime and window close on timeout
def countdown():
    global lefttime
    # Valid time
    if lefttime > 0:
        lefttime -= 1
        txt = "Time left: "+str(lefttime)
        timelabel.configure(text=txt) # replacing with updated time after each 1000ms
        timelabel.text = txt
        timelabel.after(1000, countdown) # 1s wait and then executing countdown function again
    # Invalid time
    else:
        btn.destroy() # destroying button widget
        maintext.destroy() # destroying word showing widget
        entry.configure(state='disabled') # disabling the entry widget
        entry.state = 'disables'
        # Final score display
        tk.Label(window, text="TIME OVER\nTotal score: " + str(score)).pack()
        window.after(4000, gameover) # waiting for 4s and QUIT the program

# first function to be implemented after button is clicked that check time and acts according to time left
def timecheck():
    if lefttime == 30:
        countdown()

# function to be executed after button is cicked
def btn_click(icolor):
    timecheck() # checking the current time
    global score
    global color
    txtcolor = entry.get()
    entry.delete(0, tk.END)

    # checking the textcolor and scoring based on right guess
    if txtcolor == icolor:
        score += 1
    else:
        score -= 1
        # in case of score going to be -5, Game over is displayed and window is destroyed
        if score == -5:
            btn.destroy()
            maintext.destroy()
            timelabel.destroy()
            entry.configure(state='disabled')
            entry.state = 'disables'
            tk.Label(window, text="GAME OVER, you reached minimum score").pack()
            window.after(4000, gameover)

    # updating with the score
    scr.configure(text="Score: " + str(score))
    scr.text = "Score: " + str(score)

    # changing the displayed text and color
    color = random.choice(colors)
    word = random.choice(words)
    maintext.configure(text=word, fg=color)
    maintext.text = word
    maintext.fg = color

# displaying the entry widget for user input of color guess
entry = tk.Entry(window)
entry.pack(pady=10)

# Button for checking and acting on color guess
btn = tk.Button(window, text="Verify COLOR", command=lambda: btn_click(color))
btn.pack(pady=5)

# executing mainloop() that traces the activities inside window and run the program
window.mainloop()