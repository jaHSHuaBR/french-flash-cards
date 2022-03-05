from tkinter import *
from pandas import *
from random import choice


# ---------------  GENERATE DATAFRAME AS DICT   -------------------- #
data = read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# ---------------   CONSTANTS  -------------------- #
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}


# ---------------   FUNCTIONS   -------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=card_back_img)


# ---------------   UI  -------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# ---------------   CARD CANVAS  -------------------- #
canvas = Canvas(width=800, height=526)

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
# Capturing the Canvas Img
card_img = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# # ---------------   BUTTONS  -------------------- #
right = PhotoImage(file="images/right.png")
right_btn = Button(image=right, highlightthickness=0, command=next_card)
right_btn.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)


# ---------------  MAIN LOOP WHILE USING FLASHCARDS  -------------------- #

next_card()

window.mainloop()