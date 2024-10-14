from quiz import Question, Quiz


#___tests___


mathematic_quiz = Quiz("Mathematics Quiz", "A quiz on math", [Question("What is 2 + 2?", {"3": False, "4": True, "5": False})
                                                              , Question("What is 3 + 3?", {"4": False, "5": False, "6": True})
                                                              , Question("What is 4 + 4?", {"5": False, "6": False, "8": True})])

ww2_quiz = Quiz("WW2 Russian Quiz", "A quiz about World War 2 in Russian language", [Question("Когда началась Вторая мировая война?", {"1939": True, "1941": False, "1945": False})
                                                                                            , Question("Что такое Битва за Сталинград?", {"Последняя крупная наступательная операция Советских войск": False, "Политическая борьба": False, "Одно из крупнейших сражений Второй мировой войны": True})
                                                                                            , Question("Кто командовал советскими войсками во время Великой Отечественной войны?", {"Иосиф Сталин": True, "Владимир Путин": False, "Борис Ельцин": False})
                                                                                            , Question("В каком году была подписана капитуляция нацистской Германии?", {"1945": True, "1943": False, "1941": False})])

sel_quiz = mathematic_quiz

print(len(sel_quiz.questions))
for i in range(len(sel_quiz.questions)):
    print(sel_quiz.display_current_question())
    print(i)
    answer = input("Answer: ")
    sel_quiz.next_question(answer)