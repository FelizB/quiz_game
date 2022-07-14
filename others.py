class NextQA:
    def __init__(self, dictionary):
        self.score = 0
        self.number = 0
        self.question = []
        self.answer = []

        for data in dictionary:
            self.question.append(data["text"])
            self.answer.append(data["answer"])

    def progress(self):
        if self.number < len(self.question)-1:
            return True
        else:
            return False

    def check_answer(self, answered):
        if answered == self.answer[self.number].lower():
            self.score += 1
            print(f"You got it correct. You have a score of {self.score}/{self.number} ")
            print("\n")
        else:
            print(f"you got it wrong. correct answer is {self.answer[self.number]}. "
                  f"Your score is {self.score}/{self.number}")
            print("\n")

    def next_question(self):
        next_quiz = self.question[self.number]
        self.number += 1
        answer = input(f"Q.{self.number}:{next_quiz}. (True or False): ").lower()
        self.check_answer(answer)








