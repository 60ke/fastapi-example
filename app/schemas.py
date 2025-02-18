from pydantic import BaseModel

# 请求模型
class UserCreate(BaseModel):
    name: str
    email: str

# 响应模型
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
        from_attributes = True

# 统一响应格式
class ResponseModel(BaseModel):
    code: int
    message: str
    data: dict = {}

    class Config:
        orm_mode = True