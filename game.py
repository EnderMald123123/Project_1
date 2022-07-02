from tkinter import * 
import random

root = Tk()
root.title("RPS")
width = 600
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y= (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height , x, y))
root.resizable(0,0)
root.config(bg="purple")

player_rock = PhotoImage(file='rock-user.png')
player_paper = PhotoImage(file='paper-user.png')
player_scissors = PhotoImage(file='scissors-user.png')


root.mainloop()