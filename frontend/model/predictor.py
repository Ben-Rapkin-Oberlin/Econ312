import pandas as pd
import numpy as np
import tensorflow as tf

def train_split(tile = 0.7):
    pos_tweets = pd.read_csv('pos_tweet.csv')
    neg_tweets = pd.read_csv('neg_tweet.csv')
    neg_tweets['label'] = 0

    pos_len = len(pos_tweets)
    neg_len = len(neg_tweets)

    # View the total number of positive and negative tweets.
    print(f"The number of positive tweets: {pos_len}")
    print(f"The number of negative tweets: {neg_len}")

    l = min(pos_len, neg_len)
    tile = int(l*tile)

    # Split positive set into validation and training
    val_pos   = pos_tweets[tile:]
    train_pos  = pos_tweets[:tile]

    # Split negative set into validation and training
    val_neg   = neg_tweets[tile:]
    train_neg  = neg_tweets[:tile]
    
    # # Combine training data into one set
    train = pd.concat([train_pos, train_neg], axis = 0)

    # # Combine validation data into one set
    val  = pd.concat([val_pos, val_neg], axis = 0)

    # # Separate the label and the tweet for the train set
    train_y = train['label']
    train_x = train['tweet']

    # # Separate the label and the tweet for the validation set
    val_y  = val['label']
    val_x = val['tweet']

    print(f'Number of train instances: {len(train_x)}')
    print(f'Number of positive instances: {len(train_pos)}')
    print(f'Number of negative instances: {len(train_neg)}')

    return train_pos, train_neg, train_x, train_y, val_pos, val_neg, val_x, val_y

def sentiment(trainset):
    encoder = tf.keras.layers.TextVectorization()
    encoder.adapt(trainset)
    model = tf.keras.Sequential([
        encoder,
        tf.keras.layers.Embedding(len(encoder.get_vocabulary()), 64, mask_zero=True),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,  return_sequences=True)),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1, activation = 'sigmoid')
    ])
    model.compile(loss=tf.keras.losses.BinaryCrossentropy(),optimizer=tf.keras.optimizers.Adam(1e-4),metrics=['accuracy'])
    return model

train_pos, train_neg, train_x, train_y, val_pos, val_neg, val_x, val_y = train_split()

trainset = tf.convert_to_tensor(train_x)
trainlabel = tf.convert_to_tensor(train_y)

rnn = sentiment(trainset)

sample_pos = ('The movie was cool. The animation and the graphics '
               'were out of this world. I would recommend this movie.')

callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=2)

history = rnn.fit(trainset, trainlabel, epochs=10, validation_split = 0.2, validation_steps = 30, callbacks=[callback], batch_size = 32)

prediction = rnn.predict(np.array([sample_pos]))

print(prediction)

rnn.save('model_v2')