import numpy as np
import pandas as pd
import warnings
import os

from modelDefinition import modelDef

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Input parameters in keras model:
# session_number - number of sessions with same session_id
# session_length - summed length of sessions with same session_id
# unique_products - counted unique produts with same session_id
# bought_number - counter, how many products user has bought
# labels - array with answer - whether customer bought sth or not

# load train data here
train_data = pd.read_csv("../data/processed/training_set.csv")

train_session_number = train_data['total_views']
train_session_length = train_data['time_in_minutes']
train_unique_products = train_data['unique_products']
train_unique_products_count = train_unique_products.str.count('\w+')
train_bought_number = train_data['user_bought_to_total_sessions_ratio']
train_labels = train_data['ended_with_bought']

train_session_number.to_numpy()
train_session_length.to_numpy()
train_unique_products_count.to_numpy()
train_bought_number.to_numpy()
train_labels.to_numpy()

train_data_processed = np.column_stack((train_session_number,
                                        train_session_length,
                                        train_unique_products_count,
                                        train_bought_number))

# load test data here
test_data = pd.read_csv("../data/processed/testing_set.csv")

test_session_number = test_data['total_views']
test_session_length = test_data['time_in_minutes']
test_unique_products = test_data['unique_products']
test_unique_products_count = test_unique_products.str.count('\w+')
test_bought_number = test_data['user_bought_to_total_sessions_ratio']
test_labels = test_data['ended_with_bought']

test_session_number.to_numpy()
test_session_length.to_numpy()
test_unique_products_count.to_numpy()
test_bought_number.to_numpy()
test_labels.to_numpy()

test_data_processed = np.column_stack((test_session_number,
                                       test_session_length,
                                       test_unique_products_count,
                                       test_bought_number))

# build model
model = modelDef

# train model, by adjusting model weights and minimize loss (in 5 iterations)
model.fit(train_data_processed, train_labels, epochs=5)

# evaluate model
model.evaluate(test_data_processed, test_labels, verbose=2)

# save model weights
model.save_weights('test_model_weights.h5f', overwrite=True)
