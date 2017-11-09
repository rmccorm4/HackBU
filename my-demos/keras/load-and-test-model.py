from keras.datasets import mnist
from keras.models import model_from_yaml


# Input (image) dimensions
rows, cols = 28, 28

# mnist.load_data() returns 2 tuples split into training/testing
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# If color channels are last parameter
x_train = x_train.reshape(x_train.shape[0], rows, cols, 1).astype('float32')

# Normalize pixel values between 0 and 1 per channel
x_train /= 255 

# First image in training data
random_image = x_train[0, :, :, :]

# -----------------------------------------

with open('model.yaml', 'r') as yaml_file:
	loaded_yaml_model = yaml_file.read()

# Create model from yaml config
loaded_model = model_from_yaml(loaded_yaml_model)

# Load weights
loaded_model.load_weights('model_weights.h5')
print("Loaded model and weights from disk")

prediction = loaded_model.predict(x_train)
print(prediction)
