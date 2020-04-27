# -*- coding: utf-8 -*-
from random import randrange
import numpy as np 


def relu(value):
    return max(0,value)


class Neuron:
    def __init__(self,num_inputs,activate_function,bias=True):
        self.activate_function = activate_function
        self.num_inputs = num_inputs
        self.bias = bias
        add = 0
        if bias == True:
            add = 1
        self.weights = np.array([randrange(-1000,1000) for i in range(num_inputs + add)],dtype='int64')
        
    def __agregation_function(self,inputs):
      #  print(self.weights,inputs)
        aux = self.weights * inputs
        return sum(aux)
    def resolve(self,inputs):
        inputs = list(inputs)

        if self.bias == True:
            inputs.append(1)

        inputs = np.array(inputs,dtype='int64')
        agregator = self.__agregation_function(inputs)

        return self.activate_function(agregator)


class NeuralNetworkArtificial:
    def __init__(self,num_inputs,structure_layers,activate_function,outputs_aliases=[]):
        self.structure_layers = structure_layers
        self.outputs_aliases = outputs_aliases
        self.num_inputs = num_inputs
        self.activate_function = activate_function
        self._create_structure_nna(structure_layers)
        
        
    def _create_structure_nna(self,structure_layers):
        self.num_layers = len(structure_layers)
        self.layers = []
        for num_layer in range(self.num_layers):
            layer = {'num_layer':num_layer,'neurons':[]}

            for num_neurons_in_layer in range(structure_layers[num_layer]):
                if num_layer == 0:
                    layer['neurons'].append(Neuron(self.num_inputs,self.activate_function))
                else:
                    layer['neurons'].append(Neuron(structure_layers[num_layer - 1],self.activate_function))
            
            self.layers.append(layer)
       
    def resolve(self,inputs):
        responses_layer = []
        for layer in self.layers:
            responses_layer = []
            for n in layer['neurons']:
                responses_layer.append(n.resolve(inputs))
            
            inputs = list(responses_layer)
            
        outputs = inputs
       
        if len(self.outputs_aliases) == len(self.layers[-1]['neurons']):
            outputs = {str(self.outputs_aliases[i]):outputs[i] for i in range(len(outputs))}

        return outputs

    def get_weights_nna(self):
        weights = []
        for l in self.layers:
            for n in l['neurons']:
                for w in n.weights:
                    weights.append(w)
        return weights
    
    def set_weights_nna(self,weights):
        j = 0
        for l in self.layers:
            for n in l['neurons']:
                for i in range(len(n.weights)):
                    n.weights[i] = weights[j]
                    j += 1
                  
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            