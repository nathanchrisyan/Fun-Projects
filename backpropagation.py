#Implementation of a back-propagation neural network that trains itself to do math

import math
import random

class neuralNetwork:
	def __init__(self, inputLayerLength, hiddenLayerLength, outputLayerLength, targets, a = 0.01):
		self.inputLayerLength = inputLayerLength
		self.hiddenLayerLength = hiddenLayerLength
		self.outputLayerLength = outputLayerLength
		
		self.input = []
		for i in range(inputLayerLength): #Input layer is named 'i'
			self.input.append(0) #Inserts a 0 as an initial value, and a random bias
		self.hidden = []
		for j in range(hiddenLayerLength): #Hidden layer is named 'j'
			self.hidden.append([0, random.random()])
		self.output = []	
		for k in range(outputLayerLength): #Output layer is named 'k'
			self.output.append([0, random.random()])
			
		self.weightsIH = []
		for j in range(hiddenLayerLength):
			for i in range(inputLayerLength):
				self.weightsIH.append(random.uniform(-1, 1))
		
		self.weightsHO = []
		for k in range(outputLayerLength):
			for j in range(hiddenLayerLength):
				self.weightsHO.append(random.uniform(-1, 1))
		print self.weightsHO
		self.deltak = [] #The delta values for k
		for k in range(outputLayerLength):
			self.deltak.append(0)
		self.deltaj = [] #The delta values for j
		for j in range(hiddenLayerLength):
			self.deltaj.append(0)
			
		
		self.targets = targets #The target values 
		#for k in range(outputLayerLength):
		#	self.targets.append(0)
		
		self.a = a
	
	def reset(self):
		self.input = []
		for i in range(self.inputLayerLength): #Input layer is named 'i'
			self.input.append(0) #Inserts a 0 as an initial value, and a random bias
		self.hidden = []
		for j in range(self.hiddenLayerLength): #Hidden layer is named 'j'
			self.hidden.append([0, random.random()])
		self.output = []	
		for k in range(self.outputLayerLength): #Output layer is named 'k'
			self.output.append([0, random.random()])	
	
	def Sigmoid(self, activation, p = 1.0): #The sigmoid function calculates the outputs of the neurons based on the activation
		return 1/(1 + math.e**(-activation /p))	
	
	def runNeuralNetwork(self, Input): #Runs the neural network once
		counter = 0
			
		self.input = Input	
		for j in range(len(self.hidden)): #Input to hidden computations 
			for i in range(len(self.input)):
				self.hidden[j][0] += self.input[i] * self.weightsIH[counter] #Summation of the inputs
				counter += 1
			self.hidden[j][0] += self.hidden[j][1] #Add the bias to itself
			self.hidden[j][0] = self.Sigmoid(self.hidden[j][0])
			#if self.hidden[j][0] >= 0.5:
			#	self.hidden[j][0] = 1
			#else:
			#	self.hidden[j][0] = 0			
		counter = 0
		for k in range(len(self.output)): #Hidden to output computations
			for j in range(len(self.hidden)):
				self.output[k][0] += self.hidden[j][0] * self.weightsHO[counter] #Summation of the inputs
				counter += 1
			self.output[k][0] += self.output[k][1] #Add the bias to itself
			self.output[k][0] = self.Sigmoid(self.output[k][0])
			#if self.output[k][0] >= 0.5:
			#	self.output[k][0] = 1
			#else:
			#	self.output[k][0] = 0	
	
	def setDeltak(self, set): #Sets delta k
		for k in range(self.outputLayerLength):
			self.deltak[k] = self.output[k][0] * (1 - self.output[k][0]) * (self.output[k][0] - targets[set][k])
			#print targets[set]
			
	def setDeltaj(self): #Sets delta j
		for j in range(self.hiddenLayerLength):
			Sum = 0
			for k in range(self.outputLayerLength):
				Sum += self.deltak[k] * self.weightsHO[j * self.outputLayerLength + k]
				#print Sum, "sum"
				#print j * self.outputLayerLength + k, "dank"
			self.deltaj[j] = self.hidden[j][0] * (1 - self.hidden[j][0]) * Sum
			
	def updateNeuralNetwork(self): #Updates the biases and weights of the neural network 
		for k in range(self.outputLayerLength):
			for j in range(self.hiddenLayerLength):
				self.weightsHO[k * self.hiddenLayerLength + j] += -self.a * self.deltak[k] * self.hidden[j][0]
			self.output[k][1] += -self.a * self.deltak[k]
			
		for j in range(self.hiddenLayerLength):
			for i in range(self.inputLayerLength):
				#print self.deltaj
				self.weightsIH[j * self.inputLayerLength + i] += -self.a * self.deltaj[j] * self.input[i]
				#print j * self.inputLayerLength + i
				#print -self.a * self.deltaj[j] * self.input[i]
			self.hidden[j][1] += -self.a * self.deltaj[j]	
		
	
				
targets = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
neuralnetworkstargets = []
for j in range(targets):
	tempArray = []
	for i in range(10):
		if i == targets[j]:
			tempArray.append(1)
		else:
			tempArray.append(0)
neuralnetworkstargets.append(tempArray1)

inputs = [[1, 2]]
neuralnetworkinputs.append(tempArray)
for j in range(inputs):
	tempArray = []
	for i in range(10):
		if i == inputs[j][0] or i == inputs[j][1]:
			tempArray.append(1)
		else:
			tempArray.append(0)
	neuralnetworkinputs.append(tempArray)		

newInput = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
#1 + 5, 6, 2 + 4 
 				
neuralnetwork = neuralNetwork(10, 5, 10, targets)

for i in range(1000):
	for k in range(len(inputs)):

		for p in neuralnetworkinputs[k]:
			neuralnetwork.input[p][0] = neuralnetworkinputs[][]
			
		neuralnetwork.runNeuralNetwork(neuralnetwork.input)
		neuralnetwork.setDeltak(k)
		#print neuralNetwork.deltak
		neuralnetwork.setDeltaj()
		neuralnetwork.updateNeuralNetwork()
	
		for h in range(len(neuralnetwork.input)):
			print neuralnetwork.input[h],
		print " neural network inputs"
		for p in range(len(neuralnetwork.output)):
			if neuralnetwork.output[p][0] >= 0.5:
				print 1,
			else:
				print 0,
			#print round(neuralnetwork.output[p][0], 2), 
		print " neural network output"
		for m in range(len(targets[k])):
			print neuralnetwork.targets[k][m], 
		print " target output"
		neuralnetwork.reset()

neuralnetwork.runNeuralNetwork(newInput)
for j in range(len(neuralnetwork.input)):
	print neuralnetwork.input[j],
print " neural network inputs"
for p in range(len(neuralnetwork.output)):
	if neuralnetwork.output[p][0] >= 0.5:
		print 1,
	else:
		print 0,
print " new neural network output" 
