from fastapi import FastAPI
from app.routers import user
from app.db.session import Base, engine
from app.models.user import User

app = FastAPI()

# ORM 라이브러리 불럴오기
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FastAPI with MySQL"}

# 라우터 등록
app.include_router(user.router)