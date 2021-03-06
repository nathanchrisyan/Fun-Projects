#Evolutionary Simulation of Neural Networks

#6041952301391873

#IDEA: Possible that offspring are receiving the same inputs as their parent 

import math
import random
import pygame

BACKGROUND = (255, 255, 255)
(SCREENBOUNDX, SCREENBOUNDY) = (1300, 800)
screen = pygame.display.set_mode((SCREENBOUNDX, SCREENBOUNDY))

pygame.font.init()

myfont = pygame.font.SysFont("Comic Sans MS", 13)


Food = []

count = 0
for i in range (5):
	Food.append([random.randint(0, SCREENBOUNDX), random.randint(0, SCREENBOUNDY), (225, 205, 0)])
	
Agents = []
true = 0
Update = True
Spawn = 0
WhenToUpdate = 1
TotalFitness = 0
MostFood = 0
Select = 0

Clock = pygame.time.Clock()



class Agent:
	def __init__(self, Input, Hidden, Output, posx, posy, WeightsIH, WeightsHO, Health, Color, fitness = 0):
		self.Input = Input #The Input nodes
		self.Hidden = Hidden #The Hidden nodes 
		self.Output = Output #The Output nodes
		self.WeightsIH = WeightsIH #The weights from Input to Hidden
		self.WeightsHO = WeightsHO #The weights from Hidden to Output
		self.WeightBIAS1 = random.uniform(-1, 1)
		self.WeightBIAS2 = random.uniform(-1, 1)
		self.posx = posx #The y coordinate of the agent
		self.posy = posy #The x coordinate of the agent
		self.LookAtx = 0 #The look at vector of the agent
		self.LookAty = 0 #The look at vector of the agent
		self.Rotation = 0
		self.Health = Health
		self.Ticks = 0
		self.FoodColl = 0
		self.Color = Color
		self.fitness = fitness
	def createNeuralNetwork(self): #This function creates the neural networks of each individual agent, since all connections are implied, only the weights need to be assigned
		for i in range (len(self.Input)):
			for j in range(len(self.Hidden)):
				self.WeightsIH.append(random.uniform(-2,2))
		for k in range (len(self.Hidden)):
			for l in range (len(self.Output)):
				self.WeightsHO.append(random.uniform(-2,2))
		
def Initialize(agents): #This function initalizes all of the agents, the parameter agents defines how many agents there will be
	for i in range(agents):
		Agents.append(Agent([0,0,0,0,0], [0,0,0], [0,0,0], random.randint(0, SCREENBOUNDX), random.randint(0, SCREENBOUNDY),[],[], 4000, (random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))))
		Agents[i].createNeuralNetwork() #Initialize the agent then create its neural network

def Add():
	Agents.append(Agent([0,0,0,0,0], [0,0,0], [0,0,0], random.randint(0, SCREENBOUNDX), random.randint(0, SCREENBOUNDY),[],[], 4000,(random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))))
	Agents[len(Agents) - 1].createNeuralNetwork()

def AddFood():
	Food.append([random.randint(0, SCREENBOUNDX), random.randint(0, SCREENBOUNDY), (225, 205 ,0)])
	
def Reproduction(agent):
	Agents.append(Agent([0,0,0,0,0], [0,0,0], [0,0,0], agent.posx, agent.posy, agent.WeightsIH, agent.WeightsHO, 4000 , agent.Color, agent.fitness))

	#for i in range(len(agent1.WeightsIH) - 1):
	#	Agents[len(Agents) - 1].WeightsIH[i] = (agent1.WeightsIH[i] + agent2.WeightsIH[i])/2
	#for j in range(len(agent1.WeightsHO) - 1):
	#	Agents[len(Agents) - 1].WeightsHO[j] = (agent1.WeightsHO[j] + agent2.WeightsHO[j])/2
	
def Replicate(agent):
	Agents.append(Agent([0,0,0,0,0], [0,0,0], [0,0,0], agent.posx, agent.posy ,agent.WeightsIH,agent.WeightsHO, 4000, agent.Color))
	
	
	Agents[len(Agents) - 1].WeightBIAS1 += random.uniform(-0.1, 0.1)
	
	
	Agents[len(Agents) - 1].WeightBIAS2 += random.uniform(-0.1, 0.1)
	#print len(Agents[len(Agents) - 1].WeightsIH)
	for i in range(len(Agents[len(Agents) - 1].WeightsIH)):
		
		
		Agents[len(Agents) - 1].WeightsIH[i] += random.uniform(-0.1, 0.1)
			
	for i in range(len(Agents[len(Agents) - 1].WeightsHO)):
		
		
		Agents[len(Agents) - 1].WeightsHO[i] += random.uniform(-0.1, 0.1)
	#print "happening"

def Sigmoid(activation, p = 1.0): #The sigmoid function calculates the outputs of the neurons based on the activation
	
	return 1/(1 + math.e**(-activation /p))

def CalcDistance(Pos1, Pos2):
	return math.sqrt((Pos1[0]-Pos2[0]) ** 2 + (Pos1[1] - Pos2[1]) ** 2)
	
def ClosestFood(AgentPosx, AgentPosy, Food):
	ClosestDistance = 99999999
	ClosestIndex = 99999999
	for i in range (len(Food)):
		if ((AgentPosx - Food[i][0]) ** 2 + (AgentPosy - Food[i][1]) ** 2) < ClosestDistance:
			ClosestIndex = i
			ClosestDistance = ((AgentPosx - Food[i][0]) ** 2 + (AgentPosy - Food[i][1]) ** 2)
	return ClosestIndex
		
def Clamp(Num, min, max):
	if Num > max:
		Num = max
	if Num < min:
		Num = min
	return Num
	
def Normalise(vector):
	v = math.sqrt((vector[0]**2 + vector[1]**2))
	
	
	return [vector[0]/v, vector[1]/v]	

def Roulette(TotalFitness, Agent):
	slice = random.randint(0, TotalFitness)
	
	CurrentSlice = 0
	Choose = 0
	
	for i in range(len(Agent)):
		CurrentSlice += Agent[i].fitness
		if CurrentSlice > slice:
			Choose = i
			break;
	return Choose
	
def Chromosome(Hidden, Output):
	Chromosome = []
	for i in range(len(Hidden)):
		Chromosome.append(Hidden[i])
	for i in range(len(Output)):
		Chromosome.append(Output[i])
	return Chromosome

def PushChromosome(Chromosome, Agent):
	Hidden = []
	#print Agent.WeightsIH, "hello"
	for i in range(len(Agent.WeightsIH)):
	
		Hidden.append(Chromosome[i])
	Output = []
	for j in range(len(Agent.WeightsHO), len(Chromosome)):
		Output.append(Chromosome[j])
	Agent.WeightsIH = Hidden
	Agent.WeightsHO = Output

def FindBestFitness(Agents):
	CurrentBestFitness = -999999999
	Index = 0
	for i in range(len(Agents)):
		if Agents[i].fitness > CurrentBestFitness:
			CurrentBestFitness = Agents[i].fitness
			Index = i
	return Index

def Mutate(Chromosome, MutationRate):
	for i in range(len(Chromosome)):
		Mutate = random.random()
		if Mutate < MutationRate:
			Chromosome[i] += random.uniform(-1, 1) * random.random()
	return Chromosome

	
Initialize(10) #Initialize 20 agents
#print Agents[2].WeightsIH, Agents[2].WeightsHO
print Agents[1].WeightsIH
print Agents[2].WeightsIH
print Agents[3].WeightsIH

Running = True

while Running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Running = False 
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				Update = (True, False)[Update]
			if event.key == pygame.K_s:
				WhenToUpdate += 1
			if event.key == pygame.K_z:
				WhenToUpdate -= 1
			if event.key == pygame.K_a:
				AddFood()
			if event.key == pygame.K_LEFT:
				Select += 1
				if Select > len(Agents) - 1:
					Select = len(Agents) - 1
			if event.key == pygame.K_RIGHT:
				Select -= 1
				if Select < 0:
					Select = 0
	
	Clock.tick()
	pygame.display.set_caption(str(Clock.get_fps()))
	
	#Neural network computations
	Spawn += 1
	if Spawn % 1999 == 0:
		Best = FindBestFitness(Agents)
		Reproduction(Agents[Best])
		Reproduction(Agents[Best])
	if Spawn % 2000 == 0:
		for i in range(5):
			Mum = Agents[Roulette(TotalFitness, Agents)] #Both names said in a British accent
			Dad = Agents[Roulette(TotalFitness, Agents)]
			
			#while Dad == Mum:
			#	Dad = Agents[Roulette(TotalFitness, Agents)]
			
			Mum2 = Chromosome(Mum.WeightsIH, Mum.WeightsHO)
			Dad2 = Chromosome(Dad.WeightsIH, Dad.WeightsHO)
			
			#crossover
			child1 = []
			child2 = []
			for p in range(len(Mum2)):
				child1.append(0)
				child2.append(0)
			
			Agents.append(Agent([0,0,0,0,0], [0,0,0], [0,0,0], random.randint(0, SCREENBOUNDX), random.randint(0, SCREENBOUNDY) ,[], [], 4000, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
			Agents[len(Agents) - 1].createNeuralNetwork()
			
			Agents.append(Agent([0,0,0,0,0], [0,0,0], [0,0,0], random.randint(0, SCREENBOUNDX), random.randint(0, SCREENBOUNDY) ,[], [], 4000, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
			Agents[len(Agents) - 1].createNeuralNetwork()
			
			
			CrossoverPoint = random.randint(0, len(Mum2))
			for k in range(CrossoverPoint):
				child1[k] = Mum2[k]
				child2[k] = Dad2[k]
			for j in range(CrossoverPoint, len(Mum2)):
				
				child1[j] = Dad2[j]
				child2[j] = Mum2[j]
			
			child1 = Mutate(child1, 0.1)
			child2 = Mutate(child2, 0.1)
			
			PushChromosome(child1, Agents[len(Agents) - 1])
			PushChromosome(child2, Agents[len(Agents) - 2])
			
		print TotalFitness/len(Agents), "Average Fitness"
		for i in range(12):
			del Agents[0]
			
	TotalFitness = 0
	for i in range(len(Agents)):
		
		InputFOOD = Food[ClosestFood(Agents[i].posx, Agents[i].posy, Food)]
		
		dist = CalcDistance(InputFOOD, [Agents[i].posx, Agents[i].posy])
		Agents[i].Input[0] = dist/1526
		Agents[i].Input[1] = Normalise([InputFOOD[0] - Agents[i].posx, InputFOOD[1] - Agents[i].posy])[0]
		Agents[i].Input[4] = Normalise([InputFOOD[0] - Agents[i].posx, InputFOOD[1] - Agents[i].posy])[1]
		Agents[i].Input[2] = Agents[i].LookAtx
		Agents[i].Input[3] = Agents[i].LookAty		
	
		counter = -1
		for j in range (len(Agents[i].Hidden)):
			
			for k in range (len(Agents[i].Input)):
				counter += 1
				Agents[i].Hidden[j] += Agents[i].Input[k] * Agents[i].WeightsIH[(counter)]
			Agents[i].Hidden[j] -= Agents[i].WeightBIAS1
			Agents[i].Hidden[j] = Sigmoid(Agents[i].Hidden[j])
	
		counter = -1
		for j in range(len(Agents[i].Output)):
			
			for k in range(len(Agents[i].Hidden)):
				counter += 1
				Agents[i].Output[j] += Agents[i].Hidden[k] * Agents[i].WeightsHO[counter]
			Agents[i].Output[j] -= Agents[i].WeightBIAS2			
			Agents[i].Output[j] = Sigmoid(Agents[i].Output[j])	
		TotalFitness += Agents[i].fitness		
		Agents[i].Ticks += 1
	for i in range(len(Agents)):
		lTrack = Agents[i].Output[0]
		rTrack = Agents[i].Output[1]
		
		RotForce = lTrack - rTrack
	
		RotForce = Clamp(RotForce, -1, 1)
		
		Agents[i].Rotation += RotForce
		
		Speed = Agents[i].Output[2] * 5
		
		Agents[i].LookAtx = -math.sin((Agents[i].Rotation))
		Agents[i].LookAty = math.cos((Agents[i].Rotation)) 
		Agents[i].posx += Agents[i].LookAtx * Speed
		Agents[i].posy += Agents[i].LookAty * Speed
				
		FoodToDelete = []
		
		for k in range (len(Food)):
			if CalcDistance([Agents[i].posx, Agents[i].posy], Food[k]) < 13:
				FoodToDelete.append(k)
				AddFood()
				Agents[i].Health += 1000
				Agents[i].FoodColl += 1
				Agents[i].fitness = Agents[i].FoodColl * 100
		for i in range (len(FoodToDelete)):
			del Food[FoodToDelete[i] - i]
	
	
		if Agents[i].posx > SCREENBOUNDX:
			Agents[i].posx = 0
		
		if (Agents[i].posx < 0):
			Agents[i].posx = SCREENBOUNDX
		
		if Agents[i].posy > SCREENBOUNDY:
			Agents[i].posy = 0
		
		if (Agents[i].posy < 0):
			Agents[i].posy = SCREENBOUNDY
		
		if Update:
			screen.fill(BACKGROUND)
				
		BestAgent = -123
		BestAgentIndex = 0
	if Update:
		for j in range(len(Food)):
			pygame.draw.circle(screen, Food[j][2], (int (Food[j][0]), int(Food[j][1])), 5)
	for j in range(len(Agents)):
		if Agents[j].FoodColl > MostFood:
			print "New Best!", Agents[j].FoodColl
		if Agents[j].FoodColl > BestAgent:
			BestAgent = Agents[j].FoodColl
			BestAgentIndex = j
			if BestAgent > MostFood:
				MostFood = BestAgent
			
		
		
		AgentsToDelete = []
	
	counter = -1
	for i in range(len(Agents[Select].Input)):
		for j in range(len(Agents[Select].Hidden)):
			counter += 1
			pygame.draw.line(screen, (0,0,0), (975 + i * 50 , 700), (1025 + j * 50 , 650), int(Agents[Select].WeightsIH[counter] * 2) + 1)
	counter = -1
	for i in range(len(Agents[0].Hidden)):
		for j in range(len(Agents[0].Output)):
			counter += 1
			pygame.draw.line(screen, (0,0,0), (1025 + i * 50, 650), (1025 + j * 50, 600), int(Agents[Select].WeightsHO[counter] * 2) + 1)
			
	pygame.draw.circle(screen, (Clamp(Agents[Select].Input[0] * 500, 0, 255), 0, 0), (975, 700), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Input[1] * 500, 0, 255), 0, 0), (1025, 700), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Input[2] * 500, 0, 255), 0, 0), (1075, 700), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Input[3] * 500, 0, 255), 0, 0), (1125, 700), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Input[4] * 500, 0, 255), 0, 0), (1175, 700), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Hidden[0] * 500, 0, 255), 0, 0), (1025, 650), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Hidden[1] * 500, 0, 255), 0, 0), (1075, 650), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Hidden[2] * 500, 0, 255), 0, 0), (1125, 650), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Output[0] * 200, 0, 255), 0, 0), (1025, 600), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Output[1] * 200, 0, 255), 0, 0), (1075, 600), 10)
	pygame.draw.circle(screen, (Clamp(Agents[Select].Output[2] * 300, 0, 255), 0, 0), (1125, 600), 10)
	for i in range(len(Agents)):
		
		if Agents[i].Health > 4000:
			Agents[i].Health = 4000
		
		if Update:
			
			
	
			
			pygame.draw.line(screen, (255,0,0), (Agents[i].posx, Agents[i].posy), (Agents[i].posx + Agents[i].LookAtx * 20, Agents[i].posy + Agents[i].LookAty * 20))

			if i == Select:
				pygame.draw.circle(screen, (255,0,0), (int(Agents[i].posx/1), int(Agents[i].posy/1)), 9, 1)
				pygame.draw.circle(screen, (Agents[i].Color), (int(Agents[i].posx/1), int(Agents[i].posy/1)), 8)
				pygame.draw.circle(screen, (0,0,0), (int(Agents[i].posx) + 20, int(Agents[i].posy)), 2)
			else:
				pygame.draw.circle(screen, (0,0,255), (int(Agents[i].posx/1), int(Agents[i].posy/1)), 8, 1)
				pygame.draw.circle(screen, (Agents[i].Color), (int(Agents[i].posx/1), int(Agents[i].posy/1)), 7)
		
		Agents[i].Health -= 0
		
		if Agents[i].Ticks > 2000:
			Agents[i].Ticks = 0
			
			
		
		#Agents[i].Ticks += 1.5
		if Agents[i].FoodColl >= 5:
			#Replicate(Agents[i])
				
			#Agents[i].Ticks = 0
			Agents[i].FoodColl = 0
				
		if Agents[i].Health <= 0:
			AgentsToDelete.append(i)
			
			
	for i in range(len(AgentsToDelete)):
		del Agents[AgentsToDelete[i] - i]
		
	if len(Agents) == 0:
		for i in range(5):
			Add()
		
	for i in range(WhenToUpdate):
		if Update:
			pygame.display.flip()
		
	
