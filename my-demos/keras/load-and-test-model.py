with open('model.yaml', 'r') as yaml_file:
	loaded_model = yaml_file.read()

loaded_model.load_weights('model_weights.h5')
print("Loaded model and weights from disk")


