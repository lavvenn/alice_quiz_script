from fastapi import FastAPI, Request
from quizer.quiz import Question, Quiz

from handlers import start, choice_theme, in_quiz

from pages.all_games import router

from all_quizzes import all_quizzes

app = FastAPI()

app.include_router(router)

GREETING_MESSAGE = """
Привет! Добро пожаловать в увлекательные викторины.
Готовы проверить свои знания и узнать что-то новое?
Давайте начнём! Чтобы выбрать категорию, скажите 'темы', и мы предложим вам варианты.
Удачи!
"""


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
        # обработка запросов в старотовом состоянии
        if request['state']['session']['state'] == 'start':
            start(request, response)

        # обработка запросов в состоянии выбора темы
        elif request['state']['session']['state'] == 'theme_selecting':
            choice_theme(request, response, all_quizzes)
        
        elif request['state']['session']['state'] == 'in_quiz':
            in_quiz(request, response, all_quizzes)


    return response