from fastapi import FastAPI, Request
from quizer.quiz_exampels import geo_quiz

app = FastAPI()

GREETING_MESSAGE = """
Привет! Добро пожаловать в увлекательные викторины.
Готовы проверить свои знания и узнать что-то новое?
Давайте начнём! Чтобы выбрать категорию, скажите 'категория', и мы предложим вам варианты.
Удачи!
"""

all_quizzes = {}

@app.post("/")
async def post(request: Request):
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
        response['response']['text'] = f"""вопрос: '{geo_quiz.display_current_question()["text"]}'\n
                                           варианты ответов: {', '.join(geo_quiz.display_current_question()['answers'])}"""
    else:
        response['response']['text'] = geo_quiz.next_question(request['request']['command'])

    return response