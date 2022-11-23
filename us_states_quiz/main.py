import turtle

import pandas

# Get list of states in an array
with open("50_states.csv") as states_data:
    data = pandas.read_csv(states_data)
    all_states = data["state"]

screen = turtle.Screen()
screen.title("U.S. States Quiz")

# Add new image to possible shape options for turtle
image = "blank_states_img.gif"
screen.addshape(image)
# Make a new turtle using the new image as its shape
turtle.shape(image)

# Game Loop
game_is_on = True
has_won = False
while game_is_on:
    answer_correct = False
    # Prompt User for response
    answer_state = screen.textinput(title="Guess the State", prompt="What's a name of a State")
    # Check to see if user response is correct
    for state in all_states:
        if state.lower() == answer_state.lower():
            answer_correct = state.title()
    if answer_correct:
        print("lets make that turtle")



turtle.mainloop()
