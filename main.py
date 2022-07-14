from data import question_data
from userdata import Userdata
from others import NextQA

questions = []
for data in question_data:
    question = data["text"]
    answer = data["answer"]

    userdata = Userdata(question, answer)

    userinfo = userdata.questions()
    questions.append(userinfo)
# print(questions)

next_question = NextQA(questions)
while next_question.progress():
    next_question.next_question()

print(f"You have come to the end of the questions. Your final score is {next_question.score}/{next_question.number}")
print("\n")



