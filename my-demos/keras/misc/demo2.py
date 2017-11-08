"""
Author: Ryan McCormick
File: keras_mnist.py
Purpose: Becoming familiar with Keras with a small
		 convolutional neural network
"""

import keras
from keras import backend as K
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

batch_size = 128
# Digits from 0-9
num_classes = 10
# How many times to run through the data
epochs = 12

# Input (image) dimensions
rows, cols = 28, 28

# mnist.load_data() returns 2 tuples split into training/testing
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# If color channels are last parameter
x_train = x_train.reshape(x_train.shape[0], rows, cols, 1).astype('float32')
x_test = x_test.reshape(x_test.shape[0], rows, cols, 1).astype('float32')
input_shape = (rows, cols, 1)

# Normalize pixel values between 0 and 1 per channel
x_train /= 255
x_test /= 255

# Convert class label values to one-hot vectors
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# Print out sample sizes
print("Training samples:", x_train.shape[0])
print("Test samples:", x_test.shape[0])

# Build model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

# Output layer
model.add(Dense(num_classes, activation='softmax'))

# Choosing loss function and optimizer
model.compile(loss=keras.losses.categorical_crossentropy,
			  optimizer=keras.optimizers.Adadelta(),
			  metrics=['accuracy'])

# Fit to training data
model.fit(x_train, y_train, 
		  batch_size=batch_size, 
		  epochs=epochs, 
		  verbose=1, 
		  validation_data=(x_test, y_test))

scores = model.evaluate(x_test, y_test, verbose=0)

# Print out results
print("Test loss:", score[0])
print("Test accuracy:", score[1])
