# PP5 for CS 107 pair programming
# Group members: Xin Zeng, Aleksander Aleksiev, Qinyi Chen
# Coder: Xin Zeng 
# Listener: Qinyi Chen
# Sharer: Aleksander Aleksiev

import numpy as np
import math

class Layer:
    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv

        # e.g. if shape = [2,3]
        # weights => matrix of shape [2,3]
        # bias => matrix of [1,3]
        self.weights = np.random.rand(shape[0], shape[1])
        self.bias = np.random.rand(1, shape[1])

    def forward(self, inputs):
        output = self.actv(np.dot(inputs, self.weights) + self.bias)
        return output

    def __str__(self):
        return "The shape of Layer is {}. The bias of Layer is {}.".format(self.shape, self.bias)
    
    def __repr__(self):
        return 'inputs: {}, output: {}, weights: {}, bias: {}'.format(self.shape[0], self.shape[1], self.weights, self.bias)

    def __hash__(self):
        return math.floor(np.sum(self.bias)) % 5

# Initialise test shapes
shape1 = [1,2]
shape2 = [2,4]

layer1 = Layer(shape1, np.tanh) # Define layer 1
layer2 = Layer(shape2, np.tanh) # Define layer 2

print(str(layer2)) # test __str__ is working
print(layer2.__repr__()) # test __repr__ is working 
print(layer2.__hash__()) # test __hash__ is working

inputs = np.random.rand(1, shape1[0])
h1 = layer1.forward(inputs)
h2 = layer2.forward(h1)

print(h1)
print(h2)