from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

i = 0
question_bank = []
for question in question_data:

    question_new = Question(question["question"], question["correct_answer"])
    # print(question_new.text)
    # print(question_new.answer)
    question_bank.append(question_new)
quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

quiz.finish_game()