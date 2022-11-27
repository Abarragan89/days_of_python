from tkinter import *

# Global Variables
BACKGROUND_COLOR = "#B1DDC6"

# -----------------------UI SET UP -----------------------#
window = Tk()
window.config(width=800, height=264, pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Study Cards")
# Set Up Canvas/Pictures
canvas = Canvas(width=500, height=500)
# Make PhotoImages of photo files
front_flash_card_photo = PhotoImage(file="./images/card_front.png")
back_flash_card = PhotoImage(file="./images/card_back.png")
correct_btn_photo = PhotoImage(file="./images/right.png")
incorrect_btn_photo = PhotoImage(file="./images/wrong.png")
# Create Front Flashcard
canvas.create_image(230, 240, image=front_flash_card_photo)
canvas.grid(column=0, row=0, columnspan=2)
# Create Buttons
correct_button = Button(image=correct_btn_photo, highlightthickness=0)
correct_button.grid(column=0, row=1)

incorrect_btn = Button(image=incorrect_btn_photo)
incorrect_btn.grid(column=1, row=1)

window.mainloop()
