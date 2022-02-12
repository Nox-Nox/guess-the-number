import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x320")
window.resizable(None)
window.title("Guess the number!")

rounds = 0
victory = 0
defeat = 0
Victory = IntVar()
Defeat = IntVar()
Number = IntVar()
RoundNumber = IntVar()
ResultMessage = StringVar()
ResultMessage.set("You can start")
ai_chosen_number = random.randrange(1, 10)


def reset_random_number():
    global ai_chosen_number
    ai_chosen_number = random.randrange(1, 10)
    print(f"2 AI chosen number: {ai_chosen_number}")
    return ai_chosen_number


def exit():
    window.destroy()


def main():
    global ai_chosen_number
    global rounds
    global victory
    global defeat
    number = Number.get()
    print(f"round: {rounds}")
    print(f"victories: {victory}")
    print(f"defeats: {defeat}")
    print(f"1 AI chosen number: {ai_chosen_number}")
    print(f"chosen number: {number}")

    if victory == 3 and rounds < 5:
        while number < 1 or number > 10:
            ResultMessage.set("Your guessed number is out of the given range,\n please choose a number between 1 "
                              "to 10")
            window.wait_variable(Number)
        if number == ai_chosen_number:
            ResultMessage.set("You guessed the right number!")
            rounds += 1
            RoundNumber.set(rounds)
            victory += 1
            Victory.set(victory)
            reset_random_number()
        else:
            ResultMessage.set(f"You failed, the right number was {ai_chosen_number}, try again!")
            rounds += 1
            RoundNumber.set(rounds)
            defeat += 1
            Defeat.set(defeat)
            reset_random_number()
    else:
        messagebox.showinfo("Wanna play again?")


Label(window, textvariable=RoundNumber, font='arial 20 bold').pack()
Label(window, textvariable=Victory, font='arial 20 bold').place(x=10, y=0)
Label(window, textvariable=Defeat, font='arial 20 bold').place(x=430, y=0)

Label(window, text="Pick a number", font='arial 10 bold').place(x=200, y=60)
Entry(window, textvariable=Number, font='arial 10 bold').place(x=180, y=100)

Label(window, textvariable=ResultMessage, font='arial 12 bold').pack(side=BOTTOM)

Button(window, font='arial 10 bold', text='EXIT', width=6, command=exit, bg='OrangeRed', padx=2, pady=2).place(x=10,
                                                                                                               y=160)
Button(window, font='arial 10 bold', text='CONFIRM', width=6, command=main, bg='Green', padx=2, pady=2).place(x=430,
                                                                                                              y=160)

if __name__ == '__main__':
    window.mainloop()
