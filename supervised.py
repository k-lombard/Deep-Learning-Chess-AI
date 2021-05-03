import numpy as np
import os
from keras.utils import Sequence
from keras import backend as B
from keras.layers import Dense, Input, Concatenate
from keras.models import Model, load_model



supervised_layers = [400, 200, 100, 2]


DBNpath = "./network/DBN.h5"

class Data(Sequence):
    def __init__(self, batch_size):
        self.batch_size = batch_size

        positions = np.load("./data/positions.npy")
        results = np.load('./data/results.npy')

        self.white_positions = positions[results == 1]
        self.black_positions = positions[results == 0]

        self.white_positions = self.white_positions[len(black_positions):]


        np.random.shuffle(self.white_positions)
        np.random.shuffle(self.black_positions)

        print("good so far!")

    def __len__(self):
        return int(np.ceil(len(self.black_positions)/float(self.batch_size)))

    def __getitem__(self, index):
        startIndex = index * self.batch_size

        if (startIndex + self.batch_size < len(self.black_positions)):
            w_batch = self.white_positions[startIndex : startIndex + self.batch_size]
            b_batch = self.black_positions[startIndex : startIndex + self.batch_size]
        else:
            w_batch = self.white_positions[startIndex:]
            b_batch = self.black_positions[startIndex:]


        w_results = np.ones((len(w_batch),))
        b_results = np.zeros((len(b_batch),))

        X = np.stack([w_batch, b_batch], axis = 1)

        outputs = np.stack([w_results, b_results], axis = 1)

        randomization = np.random.randint(2, size = len(X))

        X[randomization == 1] = np.flip(X[randomization == 1], axis = 1)

        outputs[randomization == 1] = np.flip(outputs[randomization == 1], axis = 1)

        batch1, batch2 = np.split(X, 2, axis = 1)

        batch1 = np.squeeze(batch1)

        batch2 = np.sqeeze(batch2)

        return [batch1, batch2], outputs


    def on_epoch_end(self):
        print("epoch over")
        np.random.shuffle(self.white_positions)
        np.random.shuffle(self.black_positions)



data_object = Data(256)

print("data object initialized")

DBN = load_model(DBNpath)

top_input = Input(shape = (774,))
bottom_input = Input(shape = (774,))


DBN_top_out = DBN(top_input)
DBN_bottom_out = DBN(bottom_input)

complete_input = Concatenate()([DBN_top_out,DBN_bottom_out])


layer1 = Dense(supervised_layers[0], activation='relu')(complete_input)
layer2 = Dense(supervised_layers[1], activation='relu')(layer1)
layer3 = Dense(supervised_layers[2], activation='relu')(layer2)
output_layer = Dense(supervised_layers[3], activation='softmax')(layer3)


pooya_and_associates_model = Model([top_input, bottom_input], output_layer)
rate = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.005,
    decay_steps=10000,
    decay_rate=0.98)
opt = keras.optimizers.Adam(learning_rate=rate)

pooya_and_associates_model.compile(optimizer = opt, loss = 'categorical_crossentropy', metrics = ['acc'])

pooya_and_associates_model.fit_generator(data_object, epochs = 200)

pooya_and_associates_model.save("./network/DeepLearningModel.h5")









