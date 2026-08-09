import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel




app = FastAPI()
class User(BaseModel):
    id: int
    name: str
    email: str



users = []

@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/")
async def get_users():
    return users

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {'message': 'user not found'}


@app.put('/users/{user_id}')
async def update_user(user_id: int, user: User):
    for i, u in enumerate(users):
        if u.id == user_id:
            users[i] = user
            return user
    return {'message': 'user not found'}

@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return {'message': 'user deleted'}
    return {'message': 'user not found'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

