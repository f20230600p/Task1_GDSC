from question import Question
from quiz import Quiz
from questions import questions

question_objects = [Question(q["text"], q["answer"]) for q in questions]
quiz = Quiz(question_objects)
quiz.play_quiz()