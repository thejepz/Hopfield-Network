# Imports
import numpy as np
import random 

# Methods
def printArrays(x1,x2,x3):
	print(x1,x1,x3)

def modSign(x):
	if (x<0):
		return -1
	else:
		return 1


# Generates an array of patterns with values of -1,1 uniformly distributed
def generatePatterns(bits,numberOfPatterns):
	patternMatrix = np.empty([bits,numberOfPatterns])
	for pattern in range(0,(numberOfPatterns)):
		for bit in range(0,(bits)):
			r = random.uniform(0,1)
			if(r<=0.5):
				patternMatrix[bit][pattern] = -1
			else:
				patternMatrix[bit][pattern] = 1
	return patternMatrix


def generateWeights(patternMatrix):
	length = len(patternMatrix)
	transposeMatrix = patternMatrix.T
	weightMatrix = np.matmul(patternMatrix,transposeMatrix)
	return (1/length*weightMatrix)

# Asynchronous update
def asynchronousUpdate(patternVector,weightMatrix,decidedBit):
	patternVectorElement = patternVector[decidedBit]
	weightMatrix = weightMatrix[decidedBit,:]
	temp = np.dot(patternVector,weightMatrix) # Problem here
	patternVector[decidedBit] = modSign(temp)





# Main 

x1 = np.array([-1,-1,-1,-1,-1,1,1,-1,-1])
x2 = np.array([-1,-1,1,-1,-1,-1,-1,1,-1])
x3 = np.array([-1,-1,-1,-1,-1,1,-1,-1,-1])

x4 = generatePatterns(10,5)
weightMatrix = generateWeights(x4)
pattern1 = x4[:,1]
pattern1 = asynchronousUpdate(pattern1,weightMatrix,1)
print(np.array_equal(x1,x2))

#P12 With non-zero diagonal of weight matrix
summa = 0
numPat = 12
for i in range(0,10):
	p12 = generatePatterns(100,numPat)
	w12 = generateWeights(p12)
	p12 = p12[:,1]
	i12 = random.randint(0,99)
	x12 = asynchronousUpdate(p12,w12,1)
	if np.array_equal(p12,x12):
		summa = summa + 1
		print(summa)
summa = summa / 100000



# Prints

