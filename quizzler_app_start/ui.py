from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=50, padx=50, bg=THEME_COLOR)
        # Score Label
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "bold"))
        self.score_label.grid(row=0, column=1)
        # Canvas Card
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Buttons
        correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_image, font=("Arial", 20, "bold"), command=self.check_true)
        self.correct_button.grid(row=2, column=0)
        incorrect_image = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(image=incorrect_image, font=("Arial", 20, "bold"), command=self.check_false)
        self.incorrect_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.correct_button.config(state="active")
            self.incorrect_button.config(state="active")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Final Score: {self.quiz_brain.score}")

    def check_false(self):
        self.correct_button.config(state="disabled")
        self.incorrect_button.config(state="disabled")
        self.ui_feedback(self.quiz_brain.check_answer("false"))

    def check_true(self):
        self.correct_button.config(state="disabled")
        self.incorrect_button.config(state="disabled")
        self.ui_feedback(self.quiz_brain.check_answer("true"))

    def ui_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
