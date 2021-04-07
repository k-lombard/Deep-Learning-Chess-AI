from tensorflow import keras
import numpy as np
import os
from keras.layers import Dense
from keras.layers import Input
from keras.models import Model
from keras import backend as B

# load the dataset
dataset = np.load("./data/positions.npy")
np.random.shuffle(dataset)
# define the keras model

print("Starting Unsupervised Training")

DBNlayers = [774, 600, 400, 200, 100]

weights = []

#Pretraining one layer at a time

for i in range(len(DBNlayers) - 1):

    print("layer training")
    print(i)

    input_layer = Input(shape = (DBNlayers[i], ))
    middle_layer = Dense(DBNlayers[i + 1], activation = 'relu')(input_layer)
    expected_output = Dense(DBNlayers[i], activation = 'relu')(middle_layer)

    opt = keras.optimizers.Adam(learning_rate = 0.005)
    model = Model(inputs = input_layer, outputs = expected_output)
    model.compile(optimizer = opt, loss = 'mse', metrics = ['mse'])
    model.fit(dataset, dataset, epochs = 200, batch_size = 256, shuffle = True)

    weights.append(model.layers[1].get_weights())

    middle_output = B.function([model.input], [model.layers[1].output])

    dataset = middle_output([dataset])[0]


input_layer = Input(shape = (DBNlayers[0],))
encoder1 = Dense(DBNlayers[1], activation = 'relu', trainable = False)(input_layer)
encoder2 = Dense(DBNlayers[2], activation = 'relu', trainable = False)(encoder1)
encoder3 = Dense(DBNlayers[3], activation = 'relu', trainable = False)(encoder2)
expected_output = Dense(DBNlayers[4], activation = 'relu', trainable = False)(encoder3)
model = Model(input_layer, expected_output)



print("building model")

for layer, weight in zip(model.layers[1:], weights):

    layer.set_weights(weight)
    layer.trainable = False

model.save(os.path.join("./network/", "DBN.h5"))

















