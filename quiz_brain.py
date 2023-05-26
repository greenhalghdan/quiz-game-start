class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            questions_remaining = True
        else:
            questions_remaining = False
        return questions_remaining

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"{self.question_number} {current_question.text} Please entre your answer: ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("correct answer")
            self.current_score += 1
        else:
            print(f"That's wrong")
        print(f"The correct answer was {correct_answer} ")
        print(f"Your current score is: {self.current_score}/{self.question_number}")
        print("\n")

    def finish_game(self):
        print("You have completed the quiz")
        print(f"Your final score was: {self.current_score}/{self.question_number}")