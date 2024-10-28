class Question:
    def __init__(self, text: str, answers: dict[str, bool],explanation_right_answer: str = ""):
        self.text = text
        self.answers = {k.lower(): v for k, v in answers.items()}
        self.explanation_right_answer = explanation_right_answer

class Quiz:
    def __init__(self, name: str, description: str, questions: list[Question],answer_options: bool = True):
        self.name = name
        self.description = description
        self.questions = questions
        
        self.answer_options = answer_options
        
        self.current_question = 0
        self.score = 0
    
    def get_current_question(self):
        question = self.questions[self.current_question]
        return {
                "text": question.text,
                "answers": list(question.answers.keys())}

    def print_current_question(self, last: bool = False):
        if self.answer_options:
            return f"""вопрос: '{self.get_current_question()["text"]}'\n
                                           варианты ответов: {', '.join(self.get_current_question()['answers'])}"""
        else:
            if self.current_question == 0:
                return f"вопрос: '{self.get_current_question()['text']}'"
            else:

                if last:
                    return f"""
                    Верно!!
                    
                    вопрос: '{self.get_current_question()["text"]}'"""

            
                else:
                    return f"""
                    неет!! {self.questions[self.current_question - 1].explanation_right_answer} \n
                    
                    вопрос: '{self.get_current_question()["text"]}'"""


        
    def check_answer(self, answer: str):
        if answer in self.questions[self.current_question].answers:
            if self.questions[self.current_question].answers[answer]:
                return True
            else:
                return False
        else:
            return False


    def next_question(self, answer: str):
        if self.check_answer(answer):
            print("Correct!")
            self.score += 1
            self.current_question += 1

            if self.current_question == len(self.questions):
                return f"вы набрали {self.score} из {len(self.questions)}."
            else:
                return self.print_current_question(True)


        else:
            print("Wrong!")
            self.current_question += 1

            if self.current_question == len(self.questions):
                return f"вы набрали {self.score} из {len(self.questions)}."
            else:
                return self.print_current_question(False)
        