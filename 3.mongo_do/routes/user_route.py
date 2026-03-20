from fastapi import APIRouter
from models.user_model import User

user_route = APIRouter(tags=["User"])

@user_route.get("/all")
async def all_user():
    users = User.find_all()
    print("users : ", users)
    data = await users.to_list()
    print("실제 데이터 : ", data)
    return data