from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    #new_question = Question(q_text=question_text, q_answer=question_answer)
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

#QuizBrain(quetion_bank)

# print(question_data[0]['text'])

# for question in range(0, len(question_data)):
#     question_bank.append(question_data[question]['text'])

# print(question_bank)