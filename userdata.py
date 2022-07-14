class Userdata:
    def __init__(self, quiz, answer):
        self.question = quiz
        self.question_answer = answer

    def questions(self):
        diction = {}
        diction["text"]= self.question
        diction["answer"] = self.question_answer

        return diction


