import turtle
from state_name import StateName
import pandas

# Get list of states in an array
data = pandas.read_csv("50_states.csv")
all_states = data["state"]

screen = turtle.Screen()
screen.title("U.S. States Quiz")

# Add new image to possible shape options for turtle
image = "blank_states_img.gif"
screen.addshape(image)
# Make a new turtle using the new image as its shape
turtle.shape(image)

# Game Loop
guessed_states = []
has_won = False
while len(guessed_states) < 50:
    # Prompt User for response
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct", prompt="What's a name of a State").title()
    # Check to see if user response is correct
    if answer_state == "Exit":
        break
    for state in all_states:
        if state == answer_state:
            guessed_states.append(state)
            winning_item = data[data.state == state]
            correct_state_display = StateName(state, float(winning_item.x), float(winning_item.y))
            break


#states to learn.csv
study_states = [state for state in all_states if state not in guessed_states]
data_frame_from_list = pandas.DataFrame(study_states)
data_frame_from_list.to_csv("states_to_study.csv")


turtle.mainloop()
