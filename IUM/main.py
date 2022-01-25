from fastapi import FastAPI
from jsonlines import jsonlines

from .models import UserEvent, Model

app = FastAPI()


def classify_client(user_event: UserEvent):
    print(user_event)
    return 1


def write_event_to_sessions(user_event: UserEvent):
    with jsonlines.open('/home/janek/Projekty/IUM/data/raw/sessions.jsonl', mode='a') as writer:
        writer.write(user_event.dict())


def write_to_log(parameters, result: int, model_type: Model):
    with jsonlines.open('output.jsonl', mode='a') as writer:
        writer.write({
            'parameters': parameters,
            'result': result,
            'model_type': model_type
        })


@app.get("/")
async def root():
    return {"message": "OK"}


@app.post("/classify/")
async def classify(user_event: UserEvent):
    write_event_to_sessions(user_event)

    return classify_client(user_event)
