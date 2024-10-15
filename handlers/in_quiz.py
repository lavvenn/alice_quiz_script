def in_quiz(request, response, all_quizzes: dict):
    response['response']['text'] = all_quizzes[request['session']['user_id']].next_question(request['request']['command'])