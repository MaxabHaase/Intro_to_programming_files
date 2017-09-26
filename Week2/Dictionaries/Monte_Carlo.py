from numpy import random

uniform = random.uniform
numSamples = 100000
numInside = 0

for i in range(numSamples):
    x, y = uniform(-1.0, 1.0, 2)

    if (x * x) + (y * y) < 1.0:
        numInside += 1

pi = 4.0 * numInside / float(numSamples)
print(pi)