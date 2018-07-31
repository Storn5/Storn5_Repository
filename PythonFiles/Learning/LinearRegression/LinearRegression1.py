import random
import numpy

#Training data set for the function y = 3x - 3
inps = [9, 13, 21, 30, 31, 31, 34, 25, 28, 20, 5]
outs = [260, 320, 420, 530, 560, 550, 590, 500, 560, 440, 300]
#Randomize weight and bias (ideally they should be 3 and -3 at the end)
weight1 = numpy.random.randn()
b = numpy.random.randn()
#Pick a small learning rate (the smaller the better, but slower)
learn_rate = 0.0001

#The function we're trying to find
def NN(inp, weight, bias):
    return (weight * inp + bias)

#Training loop
for i in range(500000):
    #Take a random data point
    i = random.randint(0, len(inps) - 1)
    #Predict the y at the point
    pred = NN(inps[i], weight1, b)
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
#Finally, print the prediction for the quest
print("Predicted formula: " + str(weight1) + "x + " + str(b))
