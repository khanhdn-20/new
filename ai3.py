import numpy as np
import math 


def sigmoid(x):
    return 1.0/(1.0 + pow(math.e,-x))

def tanh(x):
    return (pow(math.e,2*x)+1)/(pow(math.e,2*x)-1)

def softplus(x):
    return pow(math.e,x)/(1+pow(math.e,x))

def relu(x):
    return (x if x > 0 else 0)
    
def leaky_relu(x, alpha = 0.01):
    if x <= 0:
        return alpha*x
    else:
        return x

def prelu(x, alpha):
    if alpha == 0:
        return relu(x)
    else:
        return (x if x >= 0 else alpha*x)

def swish(x):
    return x*sigmoid(x)

def activate(name, x, alpha=None):
    
    # if name == "":
    if name == "sigmoid":
        return sigmoid(x)
    elif name == "tanh":
        return tanh(x)
    elif name == "softplus":
        return softplus(x)
    elif name == "relu":
        return relu(x)
    elif name == "leaky_relu":
        return leaky_relu(x,alpha)
    elif name == "prelu":
        return prelu(x,alpha)
    elif name == "swish":
        return swish(x)
    else:
        print("Wrong function")
    # else:
        # raise ValueError("Unknown activation function")

print(activate("no", math.e))
print(activate("leaky_relu", -math.e, 0.1))