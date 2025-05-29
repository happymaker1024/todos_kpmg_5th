import os
from fastapi import FastAPI, Form, Request, Depends, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine, Base
import models
app = FastAPI()

# models에 정의 한 모델 클래스, 연결한 DB에 테이블을 생성함
Base.metadata.create_all(bind=engine)

# 의존성 주입을 위한 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # 마지막에 무조건 닫음
        db.close()

abs_path = os.path.dirname(os.path.realpath(__file__))
print(abs_path)

# html 템플릿을 사용하기 위한 설정
templates = Jinja2Templates(directory=f"{abs_path}/templates")

# static 폴더과 연동하기 위한 설정
app.mount("/static", StaticFiles(directory=f"{abs_path}/static"))


@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    # todos 테이블 조회, 모든 todo를 조회
    todos = db.query(models.Todo).order_by(models.Todo.id.desc())
    # print(todos)
    for todo in todos:
        print(todo.id)
        print(todo.task)
    # html 파일에 데이터 랜더링해서 리턴한다는 의미
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "todos" : todos}
    )

# 입력한 todo를 DB에 저장하기
@app.post("/add")
async def add(request: Request,task: str = Form(...), db: Session = Depends(get_db)):
    # DB에 저장하기
    todo = models.Todo(task=task)
    db.add(todo)
    db.commit()
    # todos 조회 수행하는 path(함수)로 제어권을 넘김
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)