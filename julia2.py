import math
import pygame
from pygame.locals import*

WIDTH = 800 #If we are going at the interval of -2 to 2, there will be 4 numbers, so 800/4 = 200, 4/200 = 1/50 = 0.005, so the values will be at increments of 0.02 
HEIGHT = 800
screensize = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screensize)
iterations = 150

def clamp(var, min, max):
	if var > max:
		var = max
	if var < min:
		var = min
	return var

pixelArray = []
for i in range(800):
	tempArray = []
	for j in range(800):
		tempArray.append(0)
	pixelArray.append(tempArray)


c = -3 - 2j
z = -3-2j

counter1 = -1
counter2 = -1

for i in range(32): #We add 0.02i
	counter2 = 25 * i - 1
	counter1 = -1

	#z = -3 - 2j
	#z += 0.005j * i
	#print z, "mankus"
	for j in range(32): #We add 0.02
		c = -1.3j - 2.5
		c += 0.1j * j
		c += 0.1 * i
		counter2 = 25 * i - 1
		#counter1 = 40 * j
		#counter2 = 40 * i
		for k in range(25):
			counter2 += 1
			counter1 = 25 * j - 1
			
			for n in range(25):
				z = -1.5 -1.2j
				z += 0.15j * n
				z += 0.15 * k
				counter1 += 1
		
		
		#print i, j
		#print z
		
				for p in range(iterations):
					z = z**2 + c	
			
					#if (k == 1):
						#print z

					if (z.real > 2000000 or z.imag > 2000000):
						#print  counter1, counter2
						pixelArray[counter1][counter2] = clamp(p * 10, 0, 255)
						break;

#print pixelArray


screen.fill((255, 255, 255))

for i in range(800):
	for j in range(800):
		#print counter, j
		pygame.draw.circle(screen, (pixelArray[i][j]/2, pixelArray[i][j]/2, clamp(pixelArray[i][j] + 20, 0, 255)), (-j + WIDTH, i), 1, 1)

counter = 0
cont = True 

while (cont):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			cont = False 
			pygame.quit()
	counter += 1

	pygame.display.flip()	
				
				
	
	
