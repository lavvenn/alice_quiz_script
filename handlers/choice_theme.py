import copy

from quizer.quizes import geo_quiz, math_quiz, quiz_list




def choice_theme(request,response, all_quizzes: dict):
    if request['request']['command'] in quiz_list:

        all_quizzes[request['session']['user_id']] = copy.deepcopy(quiz_list[request['request']['command']])

        response['response']['text'] = all_quizzes[request['session']['user_id']].print_current_question()
        response['session_state'] = {'state': 'in_quiz'}


    else:
        response['response']['text'] = 'вы указали несуществующую тему. попробуйте ещё раз'
        

