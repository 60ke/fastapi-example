from fastapi import FastAPI, WebSocket, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import User
from app.schemas import UserCreate, UserResponse, ResponseModel
from app.database import Base
from app.websocket import websocket_endpoint  # 导入 WebSocket 端点

# 初始化数据库
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# WebSocket 路由
@app.websocket("/ws")
async def websocket_service(websocket: WebSocket):
    await websocket_endpoint(websocket)

@app.post("/users/", response_model=ResponseModel)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return ResponseModel(
        code=200,
        message="User created successfully",
        data={"user": UserResponse.from_orm(new_user)}
    )

@app.get("/users/{user_id}", response_model=ResponseModel)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return ResponseModel(
        code=200,
        message="User retrieved successfully",
        data={"user": UserResponse.from_orm(db_user)}
    )