from sklearn import svm
import pygame

def showResults(results):
	pygame.init()
	window = pygame.display.set_mode((256, 256))
	pygame.display.set_caption('Colors')
	colors = {'Red': (255, 0, 0), 'Green': (0, 255, 0), 'Blue': (0, 0, 255), 'Pink': (255, 127, 127), 'Orange': (255, 127, 0)}
	run = True
	red_counter = 0
	while run:
		pygame.time.delay(100)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		for i in range(0, 256, 16):
			for j in range(0, 256, 16):
				pygame.draw.rect(window, colors[results[(red_counter, i, j)]], (i, j, 16, 16))
		red_counter += 16
		if red_counter >= 256:
			red_counter = 0
		pygame.display.update()
	pygame.quit()

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
	for i in range(0, 256, 16):
		for j in range(0, 256, 16):
			for k in range(0, 256, 16):
				new_data.append([i, j, k])
	new_values = classifier.predict(new_data)
	res = {}
	for i in range(len(new_values)):
		res[tuple(new_data[i])] = new_values[i]
	showResults(res)

if __name__ == '__main__':
	main()