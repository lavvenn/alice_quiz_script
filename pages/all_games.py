# from fastapi import APIRouter, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

# from all_quizzes import all_quizzes



# templates = Jinja2Templates(directory="pages/templates")

# router = APIRouter()
# router.mount("/static", StaticFiles(directory="pages/static"), name="static")


# @router.get("/all_quizes", response_class=HTMLResponse)
# async def index(request: Request, all_quizzes: dict):
#     return templates.TemplateResponse(
#         request=request, name="all_games.html", context={"all_quizzes": str(all_quizzes)}
#     )