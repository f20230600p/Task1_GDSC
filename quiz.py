import random
from question import Question  
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def next_question(self):
        if self.questions:
            return self.questions.pop(0)
        else:
            return None

    def check_answer(self, question, user_answer):
        if question.is_correct(user_answer):
            self.score += 2
        else:
            self.score -= 1

    def questions_remain(self):
        return bool(self.questions)

    def play_quiz(self):
        self.shuffle_questions()
        while self.questions_remain():
            current_question = self.next_question()
            print(current_question.text)
            user_answer = input("True or False? ").strip()
            if user_answer.lower() in ["true", "false"]:
                self.check_answer(current_question, user_answer)
    
            else:
                print("Invalid input. Please enter 'True' or 'False'.")

        print(f"Quiz completed! Your score is: {self.score}")