class Question:
    def __init__(self, text: str, answers: dict[str, bool]):
        self.text = text
        self.answers = {k.lower(): v for k, v in answers.items()}

class Quiz:
    def __init__(self, name: str, description: str, questions: list[Question]):
        self.name = name
        self.description = description
        self.questions = questions
        
        self.current_question = 0
        self.score = 0
    
    def display_current_question(self):
        question = self.questions[self.current_question]
        return {
            "text": question.text,
            "answers": list(question.answers.keys()),}
    
    def check_answer(self, answer: str):
        if answer in self.questions[self.current_question].answers:
            if self.questions[self.current_question].answers[answer]:
                return True
            else:
                return False
        else:
            return False

    # def next_question(self, answer: str):
        
    #     if self.current_question < len(self.questions):
    #         if answer in self.questions[self.current_question - 1].answers:
    #             if self.questions[self.current_question - 1].answers[answer]:
    #                 print("Correct!")
    #                 self.score += 1
    #                 self.display_current_question()
    #             else:
    #                 print("Wrong!")
    #                 self.display_current_question()
    #         else:
    #             print("invalid answer")
    #             self.display_current_question()
    #     else:
    #         if self.questions[self.current_question - 1].answers[answer]:
    #             print("Correct!")
    #             self.score += 1
    #             self.display_current_question()
    #             print(f"You got {self.score} out of {len(self.questions)} correct.")
    #         else:
    #             print(f"You got {self.score} out of {len(self.questions)} correct.")

    def next_question(self, answer: str):
        if self.check_answer(answer):
            print("Correct!")
            self.score += 1
            self.current_question += 1
        else:
            print("Wrong!")
            self.current_question += 1

        if self.current_question == len(self.questions):
            return f"You got {self.score} out of {len(self.questions)} correct."
        else:
            return f"{self.display_current_question()["text"]}  {self.display_current_question()['answers']}"
        


# ___tests___


# mathematic_quiz = Quiz("Mathematics Quiz", "A quiz on math", [Question("What is 2 + 2?", {"3": False, "4": True, "5": False})
#                                                               , Question("What is 3 + 3?", {"4": False, "5": False, "6": True})
#                                                               , Question("What is 4 + 4?", {"5": False, "6": False, "8": True})])

# ww2_quiz = Quiz("WW2 Russian Quiz", "A quiz about World War 2 in Russian language", [Question("Когда началась Вторая мировая война?", {"1939": True, "1941": False, "1945": False})
#                                                                                             , Question("Что такое Битва за Сталинград?", {"Последняя крупная наступательная операция Советских войск": False, "Политическая борьба": False, "Одно из крупнейших сражений Второй мировой войны": True})
#                                                                                             , Question("Кто командовал советскими войсками во время Великой Отечественной войны?", {"Иосиф Сталин": True, "Владимир Путин": False, "Борис Ельцин": False})
#                                                                                             , Question("В каком году была подписана капитуляция нацистской Германии?", {"1945": True, "1943": False, "1941": False})])

# sel_quiz = mathematic_quiz

# print(len(sel_quiz.questions))
# for i in range(len(sel_quiz.questions)):
#     print(sel_quiz.display_current_question())
#     print(i)
#     answer = input("Answer: ")
#     sel_quiz.next_question(answer)

