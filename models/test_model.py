import tensorflow as tf
import numpy as np
print("TensorFlow version:", tf.__version__)

# Input parameters in keras model:
# session_number - number of sessions with same session_id
# session_length - summed length of sessions with same session_id
# unique_products - counted unique produts with same session_id
# bought_number - counter, how many products user has bought
# labels - array with answer - whether customer bought sth or not

# load train data here
train_session_number =
train_session_length =
train_unique_products =
train_bought_number =
train_labels =

train_data = np.column_stack((train_session_number, train_session_length, \
                              train_unique_products, train_bought_number))

# load test data here
test_session_number =
test_session_length =
test_unique_products =
test_bought_number =
test_labels =

test_data = np.column_stack((test_session_number, test_session_length, \
                             test_unique_products, test_bought_number))

# build model
model = th.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(1, 4)),
    tf.keras.layers.Dense(40, activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# compile model with optimizer and loss function
model.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)
)

# train model, by adjusting model weights and minimize loss (in 5 iterations)
model.fit(train_data, train_labels, epochs=5)

# ecaluate model
model.evaluate(test_data, test_labels, verbose=2)

# save model weights
model.save_weights('test_model_weights.h5f', overwrite=True)
