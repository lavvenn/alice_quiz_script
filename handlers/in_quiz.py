def in_quiz(request, response, all_quizzes: dict):
    try:
        response['response']['text'] = all_quizzes[request['session']['user_id']].next_question(request['request']['command'])

    except IndexError:
        response['response']['text'] = 'вы прошли все вопросы. если хотите начать заново, скажите "темы"'
        response['session_state'] = {'state': 'start'}