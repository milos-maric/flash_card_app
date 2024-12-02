from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------------------- DATA ---------------------------- #
try:
	data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
	original_data = pandas.read_csv("data/french_words.csv")
	to_learn = original_data.to_dict(orient="records")
else:
	to_learn = data.to_dict(orient="records")

def next_card():
	global current_card, flip_timer
	window.after_cancel(flip_timer)
	current_card = random.choice(to_learn)
	canvas.itemconfig(card_title, text="French", fill="black")
	canvas.itemconfig(card_word, text=current_card["French"], fill="black")
	canvas.itemconfig(card_background, image=front_card_image)
	flip_timer = window.after(3000, func=flip_card)

def flip_card():
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=current_card["English"], fill="white")
	canvas.itemconfig(card_background, image=back_card_image)

def is_known():
	to_learn.remove(current_card)
	data = pandas.DataFrame(to_learn)
	data.to_csv("data/words_to_learn.csv", index=False)
	next_card()

# ---------------------------- UI ------------------------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="")
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="")

#Buttons
right_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()