BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from tkinter import ttk


# ---------------------------- UI ------------------------------ #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_image = PhotoImage(file="/home/milosm/Desktop/Python-Course/flash-card-project/images/card_front.png")
canvas.create_image(400, 263	, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="French")
canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="trouve")


#Buttons
right_button_image = PhotoImage(file="/home/milosm/Desktop/Python-Course/flash-card-project/images/right.png")
wrong_button_image = PhotoImage(file="/home/milosm/Desktop/Python-Course/flash-card-project/images/wrong.png")

right_button = Button(image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)




window.mainloop()