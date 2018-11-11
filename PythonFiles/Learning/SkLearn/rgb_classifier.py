from sklearn import svm

def main():
	#Get training data
	training_data, labels = [], []
	with open('training_data.txt', 'r') as training_data_file:
		for line in training_data_file.readlines():
			training_data.append([int(x) for x in line.strip().split()])
	with open('labels.txt', 'r') as labels_file:
		for line in labels_file.readlines():
			labels.append(line.strip())
	print('Number of values: {}'.format(len(training_data)))
	print('Number of labels: {}'.format(len(labels)))
	
	#Create and train classifier
	classifier = svm.LinearSVC()
	classifier.fit(training_data, labels)
	
	#Predict new RGB values
	new_data, new_values = [], []
	for i in range(3):
		new_data.append([int(x) for x in input('New Value: ').split()])
	new_values = classifier.predict(new_data)
	print(new_data)
	print(new_values)

if __name__ == '__main__':
	main()