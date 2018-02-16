import numpy
# define the input data
input_data=numpy.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
output_data=numpy.array([[0,1,1,0]]).T

# define the data used to test the training of the machine - exam time!

testdata=numpy.array([[1,0,0]])
print ('Input training data')
print (input_data)
print ('Output training data')
print (output_data)


def initiate():

#   Initiate random weights

    numpy.random.seed(1)

    initial_set=2*numpy.random.random((3,1))-1

#  print the initial weights

    return initial_set

def sigmoid(x):
    return (1/(1+numpy.exp(-x)))

def sigmoidgrdnt (x):
    return (x*(1-x))

def calculate (x,wghts):
    return sigmoid(numpy.dot(x,wghts))

def think (input_d,w):
    
    for i in range (1,100000):
        output=calculate(input_d,w)
        error=output_data-output
# Find the adjustment value
        adjustment=numpy.dot(input_d.T,error*sigmoidgrdnt(output))
# Apply the adjustment value
        w+=adjustment
    return output,w

weights=initiate()

print ('Initial weights')
print (weights)

output,weights2=think (input_data,weights)

print ("Final weights")
print (weights2)
print("Output")
print(output)
output_data=sigmoid(numpy.dot(testdata,weights2))
print ("Output")
print (output_data)
    
    


