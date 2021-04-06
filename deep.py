from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
def initialize():
    dataset = loadtxt('training.csv', delimiter=',')
    # split into input (X) and output (y) variables
    X = dataset[:, :-2]
    y = dataset[:, -2:]
    # define the keras model
    model = Sequential()
    model.add(Dense(400, input_dim=774, activation='relu'))
    model.add(Dense(200, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation = 'softmax'))
    rate = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.01,
    decay_steps=10000,
    decay_rate=0.99) #0.004 learning rate multiplied by 0.97 after each epoch
    opt = keras.optimizers.Adam(learning_rate=rate)
    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    # fit the keras model on the dataset
    model.fit(X, y, epochs=150, batch_size=10)
def high_level_feature_extractor():
    pass



