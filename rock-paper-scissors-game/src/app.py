from tkinter import *
import random

# global Variables
round_active=True
player_score=0
computer_score=0

# Game Function
def play(user_input):
    global round_active , player_score , computer_score
    if not round_active:
        result_text.set("Click 'Next Round' to play again.")
        return
    
    dict1 = {"r": 1, "p": 0, "s": -1}
    dict2 = {1: "Rock", 0: "Paper", -1: "Scissors"}
    computer = random.choice([-1, 0, 1])
    you = dict1[user_input]
    comp_choice = dict2[computer]
    user_choice = dict2[you]

    if computer == you:
        result = "It's a draw."
    elif (computer == 1 and you == 0) or (computer == -1 and you == 1) or (computer == 0 and you == -1):
        result = "You win!!"
        player_score += 1
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        result = "You lose!!"
        computer_score += 1
    else:
        result = "Something went wrong..."
    result_text.set(f"Computer chose: {comp_choice}\nYou chose: {user_choice}\n\n{result}")
    round_active =False

# New round function
def new_round():
    global round_active
    round_active=True
    result_text.set("New round started!")

# Score function
def score():
    global player_score,computer_score
    result_text.set(f"Computer Score: {computer_score} | Player Score: {player_score} ")

# Exit function
def close_game():
    root.destroy()

# GUI Setup
root=Tk()
root.title("Rock , Paper & Scissors Game")
root.geometry("600x400")
root.resizable(0,0)

root_label = Label(root, text="Rock , Paper & Scissors Game", font=("Times New Roman", 16))
root_label.pack(pady=10)

f1 = Frame(root,borderwidth=6)
f1.pack(pady=20)

# Buttons
b1=Button(f1, text="Rock", width=10, font=("Times New Roman", 12), command=lambda: play("r"))
b1.grid(row=0, column=0, padx=10)

b2=Button(f1, text="Paper", width=10, font=("Times New Roman", 12), command=lambda: play("p"))
b2.grid(row=0, column=1, padx=10)

b3=Button(f1, text="Scissors", width=10, font=("Times New Roman", 12), command=lambda: play("s"))
b3.grid(row=0, column=2, padx=10)

b4=Button(f1, text="Next Round", width=10, font=("Times New Roman", 12), command=new_round)
b4.grid(row=1, column=0, columnspan=3, pady=5)

b6=Button(f1, text="score", width=10, font=("Times New Roman", 12), command=score)
b6.grid(row=2, column=0, columnspan=3, pady=5)

b5=Button(f1, text="Exit", width=10, font=("Times New Roman", 12), command=close_game)
b5.grid(row=3, column=0, columnspan=3, pady=5)

result_text = StringVar()
result_text.set("Choose Rock, Paper or Scissors to Start!")
result_label = Label(root, textvariable=result_text, font=("Times New Roman", 12), justify="center")
result_label.pack(pady=20)

root.mainloop()