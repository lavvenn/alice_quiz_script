from quizer.quizes import quiz_list

def start(request, response):
    if request['request']['command'] == 'темы':
        response['session_state'] = {'state': "theme_selecting"}
        response['response']['text'] = 'выберите тему'
        response['response']['buttons'] = [{'title': i, 'hide': False} for i in quiz_list.keys()]

    elif request['request']['command'] == 'информация':
        response['response']['text'] = 'информация'

    else:
        response['response']['text'] = 'не поняла вас. вы хотмте выбрать тему или узнать информацию?'