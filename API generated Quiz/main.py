from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


AMOUNT = 10
PARAMETER={
    "type": "boolean",
    "amount": AMOUNT,
}
response = requests.get(url="https://opentdb.com/api.php",params=PARAMETER)
response.raise_for_status()

data = response.json()

question_bank = []
for i in range (0,AMOUNT):
    question_text = data['results'][i]['question']
    question_answer = data['results'][i]['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)  #taking quiz as input to make question text visible in gui


'''while quiz.still_has_questions():
    quiz.next_question()'''

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
