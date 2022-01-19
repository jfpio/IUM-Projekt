from fastapi import FastAPI
from pydantic import BaseModel
from ..models import predictPurchase

app = FastAPI()


class UserEvent(BaseModel):
    session_id: int
    user_id: int
    product_id: int


def classify_client(user_event: UserEvent):
    print(user_event)
    return 1


@app.get("/")
async def root():
    return {"message": "OK"}


@app.post("/classify/")
async def classify(user_event: UserEvent):
    return classify_client(user_event)
