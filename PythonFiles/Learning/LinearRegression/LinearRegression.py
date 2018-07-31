import random
import numpy
import matplotlib.pyplot as plt

#Training data set for the function y = 3x - 3
inps = [-1, 0, 1, 2, 3]
outs = [-5, -3, -1, 3, 7]
#We want to find the y of this x
quest = 5
#Randomize weight and bias (ideally they should be 3 and -3 at the end)
weight1 = numpy.random.randn()
b = numpy.random.randn()
#Pick a small learning rate (the smaller the better, but slower)
learn_rate = 0.1

#The function we're trying to find
def NN(inp, weight, bias):
    return (weight * inp + bias)

#Training loop
while True:
    #Take a random data point
    i = random.randint(0, 4)
    #Predict the y at the point
    pred = NN(inps[i], weight1, b)
    print("Error: " + str(pred - outs[i]))
    #Find the derivative of the square of the error w. r. t. the error
    #   dErrSq_dErr = 2 * (pred-outs[i])
    #Find the derivative of the error w. r. t. the weight
    #   dErr_dWeight = inps[i]
    #Find the derivative of the error w. r. t. the bias
    #   dErr_dBias = 1
    #Find the derivative of the square of the error w. r. t. the weight
    dErrSq_dWeight = 2 * (pred - outs[i]) * inps[i]
    #Find the derivative of the square of the error w. r. t. the bias
    dErrSq_dBias = 2 * (pred - outs[i])
    #Adjust the weight and bias slightly
    weight1 -= learn_rate * dErrSq_dWeight
    b -= learn_rate * dErrSq_dBias
    #Stop if asked
    if input() == "stop":
        break
#Finally, print the prediction for the quest
plt.plot(inps, outs, "ro")
plt.plot([-5, 10], [NN(-5, weight1, b), NN(10, weight1, b)], "b-")
plt.plot([quest], [NN(quest, weight1, b)], "go")
plt.show()
print("The expected value is 12. The predicted value is " + str(NN(quest, weight1, b)))
