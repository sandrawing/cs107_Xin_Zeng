# Coder: Xin Zeng
# Listener: Will Wang
# Sharer: Morris Reeves

#The outer function should return a layer object (the inner function). It should take in two arguments:
    #shape: A list of two numbers where the first number is the number of inputs to the layer and the second number is the number of units in the layer.
    #actv: An activation function (remember, functions are first class in Python!)
#The inner function should return the layer outputs.
    #Remember, the layer outputs are the outputs of each unit in the layer.
    #This function should take in three arguments:
        #inputs: The inputs to the layer. This should be a numpy array.
        #weights: The weights for this layer. This should be a matrix of size shape.
        #bias: The bias for each unit in this layer. This should be a vector of size shape[1] (the number of units in the layer).

import numpy as np

def layer(shape, actv):
    def inner(inputs, weights, bias):
        x = np.dot(inputs, weights) + bias
        return actv(x)
    return inner


t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network: (1, 100)
# print("t: ", t)
unit0 = t.shape[1]
unit1 = 5
unit2 = 2
shape1 = (unit0,unit1)
shape2 = (unit1,unit2)

layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.random.rand(t.shape[1],unit1)/100
# print("w1: ", w1)
w2 = np.random.rand(unit1,unit2)/100
b1 = np.random.rand(1,unit1)
b2 = np.random.rand(1,unit2)

# Run through the network
h1 = layer1(t, w1, b1) # First layer
print('h1: ',h1)
h2 = layer2(h1, w2, b2) # Last layer
print('h2: ',h2)

## Contention 1: What is the shape?
# input: （1, 100) or (1,unit0)
# weights: (100, 5) or (unit0,unit1)
# bias: (1, 5) or (1,unit1)
# inner's output: (1, unit1) or same as bias

## Contention 2: Debugging (first outputs for h1 and h2): confirmed that tanh returns 1 for many values of x, so first layer is working as expected
## Testing on small values of w1 and w2 yields non-1 values of h1, as expected
#h1:  [[0.5154857  0.57693399 0.31614326 0.52894368 0.42910693]]
#h2:  [[0.26921517 0.12077364]]