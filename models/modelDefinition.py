import tensorflow as tf

modelDef = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_dim=4),
    tf.keras.layers.Dense(10, activation='tanh'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(12, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# compile model with optimizer and loss function
modelDef.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.BinaryCrossentropy(from_logits=False),
    metrics=['accuracy']
)
