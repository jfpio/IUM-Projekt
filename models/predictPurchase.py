import tensorflow as tf
import os.path
from modelDefinition import modelDef

def predictPurchase(modelInput):
    model = modelDef
    if os.path.exists('dqn_weights.h5f'):
        model.load_weights('dqn_weights.h5f')
    return model(modelInput)
