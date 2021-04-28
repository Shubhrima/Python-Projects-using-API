THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):    #quiz_brain:QuizBrain means the quiz_brain imported is of datatype QuizBrain
        self.quiz=quiz_brain
        self.window= window = Tk()
        self.window.title("QUIZ")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score=Label(text="Score: 0", font=("Courrier", 10, "bold"), fg='white',bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.quote_text = self.canvas.create_text(150, 125, text='Question goes here', font=("Arial", 15, "italic"), width=250,
                                             fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)


        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, command=self.opted_false, highlightthickness=0)
        self.wrong_button.grid(row=2, column=0)

        correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_image, command=self.opted_true, highlightthickness=0)
        self.correct_button.grid(row=2, column=1)



        self.get_next_question()
        self.window.mainloop()



    def opted_true(self):
        is_right=self.quiz.check_answer("True")
        self.feedback(is_right)

    def opted_false(self):
        is_right=self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right==True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)


    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=question_text)
        else:
            self.canvas.itemconfig(self.quote_text, text=f'The quiz is over. You scored {self.quiz.score}.')