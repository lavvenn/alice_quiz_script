from fastapi import FastAPI, Request
from quizer.quiz_exampels import geo_quiz
from quizer.quiz import Question, Quiz

app = FastAPI()

GREETING_MESSAGE = """
Привет! Добро пожаловать в увлекательные викторины.
Готовы проверить свои знания и узнать что-то новое?
Давайте начнём! Чтобы выбрать категорию, скажите 'темы', и мы предложим вам варианты.
Удачи!
"""

all_quizzes = {}

@app.post("/")
async def post(request: Request):
    global all_quizzes
    print(all_quizzes)

    request = await request.json()
    response = {
        'session': request['session'],
        'version': request['version'],
        'session_state': request.get('state', {}).get('session', {}),
        'response': {
            'end_session': False,
            'text': GREETING_MESSAGE
        }
    }

    print(request)
    
    if request['session']['new']:
        response['session_state'] = {"state": "start"}
        response['response']['text'] = GREETING_MESSAGE
    else:
        if request['state']['session']['state'] == 'start':

            if request['request']['command'] == 'темы':
                response['session_state'] = {'state': "theme_selecting"}
                response['response']['text'] = 'выберите тему'
                response['response']['buttons'] = [
                    {
                        'title': 'География',
                        'hide': False
                    },
                    {
                        'title': 'Математика',
                        'hide': False
                    }]

            elif request['request']['command'] == 'информация':
                response['response']['text'] = 'информация'

            else:
                response['response']['text'] = 'не поняла вас. вы хотмте выбрать тему или узнать информацию?'

        elif request['state']['session']['state'] == 'theme_selecting':
            print("allllloo")
            if request['request']['command'] == 'география':
                print("allllloo222")
                response['session_state']["state"] = "in_quiz"
                all_quizzes[request['session']['user_id']] = Quiz("геогрфия квиз", "Квиз на геогрфию", [Question("Какая столица Франции?", {"Париж": True, "Лондон": False, "Берлин": False}),
                    Question("Какая столица Германии?", {"Париж": False, "Лондон": False, "Берлин": True}),
                    Question("Какая столица Англии?", {"Париж": False, "Лондон": True, "Берлин": False})])
                response['response']['text'] = all_quizzes[request['session']['user_id']].print_current_question()
        
        elif request['state']['session']['state'] == 'in_quiz':
            response['response']['text'] = all_quizzes[request['session']['user_id']].next_question(request['request']['command'])


    return response