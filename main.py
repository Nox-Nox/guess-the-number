import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x320")
window.resizable(None)
window.title("Guess the number noob :3")

rounds = 0
victory = 0
defeat = 0
Victory = IntVar()
Defeat = IntVar()
Number = IntVar()
RoundNumber = IntVar()
ResultMessage = StringVar()
ResultMessage.set("Are you retarded? just start already LMAO")
ai_chosen_number = random.randrange(1, 10)


def reset_random_number():
    global ai_chosen_number
    ai_chosen_number = random.randrange(1, 10)
    print(f"2 AI chosen number: {ai_chosen_number}")
    return ai_chosen_number


def exit():
    window.destroy()


def log(number):
    print(f"round: {rounds}")
    print(f"victories: {victory}")
    print(f"defeats: {defeat}")
    print(f"1 AI chosen number: {ai_chosen_number}")
    print(f"chosen number: {number}")


def reset_game():
    global rounds
    global victory
    global defeat
    rounds = 0
    victory = 0
    defeat = 0
    Number.set(0)
    Victory.set(0)
    Defeat.set(0)
    RoundNumber.set(0)


def main():
    global ai_chosen_number
    global rounds
    global victory
    global defeat
    number = Number.get()
    log(number)
    while number < 1 or number > 10:
        ResultMessage.set(
            f"Yo wtf? can't you read? is {number} a number between the given range?\n please be less autistic and "
            f"choose a number between 1 to 10 ")
        if number < 1 or number > 10:
            window.wait_variable(Number)

    if number == ai_chosen_number:
        ResultMessage.set("Wow... what an alpha man...")
        rounds += 1
        RoundNumber.set(rounds)
        victory += 1
        Victory.set(victory)
        reset_random_number()
    else:
        ResultMessage.set(
            f"You failed lol, the right number was {ai_chosen_number} dumbness, \n try again if you wanna "
            f"feel even more stupid")
        rounds += 1
        RoundNumber.set(rounds)
        defeat += 1
        Defeat.set(defeat)
        reset_random_number()

    if victory == 3:
        messagebox.showinfo("Game result", "Oh... you are actually amazing... wanna go on a date with me? *blush*")
        reset_game()
    if defeat == 3:
        messagebox.showinfo("Game result", "LMAO WHAT A LOSER, don't you ever try again just press the exit button "
                                           "and go play Minecraft LMAO")
        reset_game()


Label(window, text="Round", font='arial 20 bold').pack()
Label(window, textvariable=RoundNumber, font='arial 20 bold').pack()

Label(window, textvariable=Victory, font='arial 20 bold').place(x=110, y=0)
Label(window, text="Victories:", font='arial 18 bold').place(x=0, y=0)

Label(window, textvariable=Defeat, font='arial 20 bold').place(x=478, y=0)
Label(window, text="Defeats:", font='arial 18 bold').place(x=382, y=0)

Label(window, text="PiCk A nUmBeR BeTwEeN 1 tO 10", font='arial 14 bold').place(x=115, y=100)
Entry(window, textvariable=Number, font='arial 10 bold').place(x=180, y=140)

Label(window, textvariable=ResultMessage, font='arial 12 bold').pack(side=BOTTOM)

Button(window, font='arial 10 bold', text='EXIT', width=6, command=exit, bg='Red', padx=2, pady=2).place(x=10,
                                                                                                         y=200)
Button(window, font='arial 10 bold', text='CONFIRM', width=6, command=main, bg='Green', padx=2, pady=2).place(x=430,
                                                                                                              y=200)
Button(window, font='arial 10 bold', text='RESTART', width=6, command=reset_game, bg='Grey', padx=2, pady=2).place(
    x=220,
    y=200)

if __name__ == '__main__':
    window.mainloop()
