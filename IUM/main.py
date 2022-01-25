from random import randrange

from fastapi import FastAPI
from jsonlines import jsonlines

from models.predictPurchase import basic_prediction_model, predict_purchase
from .data.main import prepare_data_to_model_request
from .models import UserEvent, DataToModel

app = FastAPI()


def write_event_to_sessions(user_event: UserEvent):
    with jsonlines.open('/home/janek/Projekty/IUM/data/raw/sessions.jsonl', mode='a') as writer:
        writer.write(user_event.dict())


def write_to_log(data_to_model: DataToModel, result: int, model_type: str):
    with jsonlines.open('output.jsonl', mode='a') as writer:
        writer.write({
            'parameters': data_to_model._asdict(),
            'result': result,
            'model_type': model_type
        })


@app.get("/")
async def root():
    return {"message": "OK"}


@app.post("/classify/")
async def classify(user_event: UserEvent):
    write_event_to_sessions(user_event)
    data_to_model_request = prepare_data_to_model_request(user_event)

    if randrange(2) % 2:
        result = predict_purchase(data_to_model_request)
        write_to_log(
            data_to_model_request, result, "NN_MODEL"
        )
    else:
        result = basic_prediction_model(data_to_model_request)
        write_to_log(
            data_to_model_request, result, "BASIC_MODEL"
        )

    return result
