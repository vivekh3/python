from numpy import array,dot,exp,random

class neural_layer():
    def __init__(self,number_of_neurons,number_inputs_per_neuron):
        self.neuralweights = 2*random.random((number_inputs_per_neuron,number_of_neurons))-1

class  neural_networks():
    def __init__(self,hidden_layer,layer2):
        self.hidden_layer=hidden_layer
        self.layer2=layer2

    def __sigmoid(self,x):
        return (1/(1+exp(-x)))

    def __sigmoidgrad(self,x):
        return (x*(1-x))

    def think(self,inputs):
        neth=array(dot(inputs,self.hidden_layer.neuralweights))
        output_from_hidden_layer=self.__sigmoid(neth)

        neto=array(dot(output_from_hidden_layer,self.layer2.neuralweights))
        output_from_layer_2=self.__sigmoid(neto)

        return output_from_hidden_layer,output_from_layer_2

    
    def train(self,training_inputs, training_outputs, number_of_iterations):
        for iteration in range(number_of_iterations):
            output_from_hidden_layer,output_from_layer_2 = self.think(training_inputs)
# The following few lines are nothing but calculation of d(Error)/d(Ai) and d(Error)/d(Wi)
            layer2_error=training_outputs-output_from_layer_2

            layer2_delta=layer2_error*self.__sigmoidgrad(output_from_layer_2)

            hidden_layer_error=layer2_delta.dot(self.layer2.neuralweights.T)
            hidden_layer_delta=hidden_layer_error*self.__sigmoidgrad(output_from_hidden_layer)
            
# Just to reinforce from the theory above, hidden layer adjustment = d(Error)/d(Wi ) =
# (d(Error)/d(Output)) * (d(Output)/d(Neto )) * (d(Neto )/d(Outputh )) * (d(Outputh )/d(Neth )) * (d(Neth )/d(Wi ))
# or d(Error)/d(Wi ) = (Output - Target)*(Output*(1-Output))*Ai *(Outputh *(1-Outputh ))*Xi
# Similarly Layer 2 adjustment = d(Error)/d(Ai ) = -1*(Target-Output) * (Output*(1-Output))*Outputh 

            hidden_layer_adjustment=training_inputs.T.dot(hidden_layer_delta)
            layer2_adjustment=output_from_hidden_layer.T.dot(layer2_delta)

            self.hidden_layer.neuralweights+=hidden_layer_adjustment
            self.layer2.neuralweights+=layer2_adjustment

    def print_weights(self):
        print ("Weights for hidden_layer")
        print (self.hidden_layer.neuralweights)
        print ("Weights for Layer 2")
        print ((self.layer2.neuralweights))
                


if __name__=="__main__":
    random.seed(1)
# Initializing layers
    hidden_layer=neural_layer(4,3)
    layer2=neural_layer(1,4)
    neural_network = neural_networks(hidden_layer,layer2)
# Initializing weights
    print ("Starting weights")
    neural_network.print_weights()
# Intializing input and target output
    training_set_inputs = array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    training_set_outputs = array([[1, 1, 1, 0, 0, 1, 0]]).T
# Training begins
    neural_network.train(training_set_inputs,training_set_outputs,100000)
    print ("Ending weights")
    neural_network.print_weights()
# Now for the exam.!
    print ("Output")
    hidden_state,output=neural_network.think(array([0,1,0]))
    print (output)


