import math
import pygame
from pygame.locals import*

WIDTH = 800 #If we are going at the interval of -2 to 2, there will be 4 numbers, so 800/4 = 200, 4/200 = 1/50 = 0.005, so the values will be at increments of 0.02 
HEIGHT = 800
screensize = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screensize)

pixelArray = []
for i in range(800):
	tempArray = []
	for j in range(800):
		tempArray.append(0)
	pixelArray.append(tempArray)


c = -4 + -0.010j 
for i in range(800): #We add 0.02i
	c = -3 - 2j
	c += 0.005j * i
	for j in range(800): #We add 0.02
		c += 0.005
		z = 0
		
		#print i, j
		
		for k in range(100):
			z = z**2 + c
			
			if ((z.real > 100 or z.imag > 100) and k < 10):
				pixelArray[i][j] = 1000
				break;
			
			if ((z.real > 100 or z.imag > 100) and k < 30 and k > 10):
				pixelArray[i][j] = 1
				break;
			elif (((z.real > 100 or z.imag > 100) and k < 50 and k > 30)):
				pixelArray[i][j] = 2
				break;
			elif (((z.real > 100 or z.imag > 100) and k < 70 and k > 50)):
				pixelArray[i][j] = 3
				break;
			elif (((z.real > 100 or z.imag > 100) and k <= 100 and k > 70)):
				pixelArray[i][j] = 4
				break;

#print pixelArray


screen.fill((255, 255, 255))
for i in range(800):
	for j in range(800):
		#print counter, j
		if pixelArray[i][j] == 0:
			pygame.draw.circle(screen, (0, 0, 0), (-j + WIDTH, i), 1, 1)
		
		elif pixelArray[i][j] == 1:
			pygame.draw.circle(screen, (255, 70, 70), (-j + WIDTH, i), 1, 1)
		
		elif pixelArray[i][j] == 2:
			pygame.draw.circle(screen, (220, 50, 50), (-j + WIDTH, i), 1, 1)
		
		elif pixelArray[i][j] == 3:
			pygame.draw.circle(screen, (120, 70, 70), (-j + WIDTH, i), 1, 1)
		
		elif pixelArray[i][j] == 4:
			pygame.draw.circle(screen, (0, 0, 0), (-j + WIDTH, i), 1, 1)

		else:
			pygame.draw.circle(screen, (255, 0,0), (-j + WIDTH, i), 1, 1)

counter = 0
cont = True 

while (cont):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			cont = False 
			pygame.quit()

	pygame.display.flip()	
				
				
	
	
