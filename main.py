from tkinter import *
import random
root = Tk()

root.title("Rock Paper Scissor :- Abhinav Kumar Prajapati")
root.geometry("200x200")
def Working(num):
    button_1.configure(bg = "white")
    button_2.configure(bg = "white")
    button_3.configure(bg = "white")
    com_choice = random.randint(1,3)
    
    if com_choice == 1:
        button_1.configure(bg = "yellow")
    
    elif com_choice == 2:
        button_2.configure(bg = "yellow")
    
    elif com_choice == 3:
        button_3.configure(bg = "yellow")
    winner(num,com_choice)
    
def winner(a,b):
    if a == b:
        Result.configure(text = "Draw")
    elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        Result.configure(text = "You Won")
    else:
        Result.configure(text = "Computer Won")
comp_label = Label(text = "Computer's choice").pack(side = "top")
button_1 = Button(root, text = "Rock", state = "disabled")
button_1.place(anchor = "center", relx = 0.2, rely = 0.2)

button_2 = Button(root, text = "Paper", state = "disabled")
button_2.place(anchor = "center", relx = 0.5, rely = 0.2)

button_3 = Button(root, text = "Scissor", state = "disabled")
button_3.place(anchor = "center", relx = 0.8, rely = 0.2)

button_4 = Button(root, text = "Rock", state = "active", command = lambda: Working(1))
button_4.place(anchor = "center", relx = 0.2, rely = 0.9)

button_5 = Button(root, text = "Paper", state = "active", command = lambda: Working(2))
button_5.place(anchor = "center", relx = 0.5, rely = 0.9)

button_6 = Button(root, text = "Scissor", state = "active", command = lambda: Working(3))
button_6.place(anchor = "center", relx = 0.8 , rely = 0.9)

Result = Label(text = "Choose Your option !!! ",bg = "yellow", fg = "red")
Result.place(anchor = "center", relx = 0.5, rely = 0.5)


root.mainloop()