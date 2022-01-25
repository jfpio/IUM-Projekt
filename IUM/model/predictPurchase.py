import os.path
from IUM.model.modelDefinition import modelDef
import numpy as np

def predict_purchase(model_input):
    model = modelDef
    if os.path.exists('dqn_weights.h5f'):
        model.load_weights('dqn_weights.h5f')
    return float(model.predict(np.array(model_input).reshape(1,4))[0][0])


def basic_prediction_model(model_input):
    if 10 <= model_input[1] <= 15:
        return 1
    else:
        return 0
