import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


no_of_question=int(input("Enter the no of questions you want to have for your quiz: "))
question_bank=[]
for x in range(0,no_of_question):
    questions=random.choice(question_data)
    question_text=questions["question"]
    question_answer=questions["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("yay! you have completed your Quiz")
print(f"Your Final Score is {quiz.score}/{len(question_bank)}")
