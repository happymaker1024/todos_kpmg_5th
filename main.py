import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

abs_path = os.path.dirname(os.path.realpath(__file__))
print(abs_path)

# html 템플릿을 사용하기 위한 설정
templates = Jinja2Templates(directory=f"{abs_path}/templates")

# static 폴더과 연동하기 위한 설정
app.mount("/static", StaticFiles(directory=f"{abs_path}/static"))


@app.get("/")
async def home(request: Request):
    todo = 20
    # html 파일에 데이터 랜더링해서 리턴한다는 의미
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "todo" : todo}
    )