from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if REPS == 10:
        count_down(LONG_BREAK_MIN)  # multiply by 60 before finishing
        timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN)
        timer_label.config(text="Work", fg=GREEN)


# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    # if count < 0:
    #     start_timer()
    minutes_left = count // 60
    minutes_left = str(minutes_left).rjust(2, '0')
    seconds_left = count % 60
    seconds_left = str(seconds_left).rjust(2, '0')
    display_time = f"{minutes_left}:{seconds_left}"
    canvas.itemconfig(timer_text, text=display_time)
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        number_of_checks = REPS // 2
        checks = "".rjust(number_of_checks, '✔')
        check_mark.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Title Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
timer_label.grid(column=1, row=0)


# Start/Reset Buttons
start_btn = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", bg="white", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "normal"))
check_mark.grid(column=1, row=3)

window.mainloop()
