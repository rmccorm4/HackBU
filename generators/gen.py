def training_generator():
	window = 5
	for i in range(0, len(diffs) - window):
		yield {j : diffs.iloc[i+j] for j in range(window) }

generator = training_generator()

df = pd.DataFrame(generator)


m sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier
clf.fit(examples, answers)
predictions = clf.predict(examples)


cool pandas thing
data.askPrice[data.askPrice > 149], filters data to condition
