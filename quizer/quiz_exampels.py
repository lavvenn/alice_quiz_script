from quizer.quiz import Question, Quiz

mathematic_quiz = Quiz("Mathematics Quiz", "A quiz on math", [Question("What is 2 + 2?", {"3": False, "4": True, "5": False})
    , Question("What is 3 + 3?", {"4": False, "5": False, "6": True})
    , Question("What is 4 + 4?", {"5": False, "6": False, "8": True})])

geo_quiz = Quiz("геогрфия квиз", "Квиз на геогрфию", [Question("Какая столица Франции?", {"Париж": True, "Лондон": False, "Берлин": False})
    , Question("Какая столица Германии?", {"Париж": False, "Лондон": False, "Берлин": True})
    , Question("Какая столица Англии?", {"Париж": False, "Лондон": True, "Берлин": False})])
