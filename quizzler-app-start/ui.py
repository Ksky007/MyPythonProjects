from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        self.window = Tk()
        self.window.title = 'Quiz APP'
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.text = self.canvas.create_text(150, 125,
                                            width=280,
                                            text='Some question texts',
                                            fill=THEME_COLOR,
                                            font=('Arial', 15, 'italic'))

        self.label = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white', font=('Arial', 12, 'italic'))
        self.label.config(pady=10)
        self.label.grid(column=1, row=0)

        t = PhotoImage(file='images/true.png')
        self.button1 = Button(image=t, bg=THEME_COLOR, command=self.right)
        self.button1.grid(column=0, row=2)

        f = PhotoImage(file='images/false.png')
        self.button2 = Button(image=f, bg=THEME_COLOR, command=self.wrong)
        self.button2.grid(column=1, row=2)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.text, text='You have reached the end of the questions~')
            self.button1.config(state='disable')
            self.button2.config(state='disable')

    def right(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            print("you are right")
            self.canvas.config(bg='green')
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            print("you are wrong")
            self.canvas.config(bg='red')

        self.window.after(1000, func=self.next_one)

    def next_one(self):
        self.canvas.config(bg='white')
        self.get_question()