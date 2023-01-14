#graph this info
#stocks in a csv file

from bs4 import BeautifulSoup
import requests
import pygame
from pygame.locals import *

#get the page
page = requests.get("https://en.wikipedia.org/wiki/List_of_Chelsea_F.C._seasons")

#parse it
soup = BeautifulSoup(page.content, 'html.parser')

#used in while loop to end the loop
check = 0

#length of the bar containing data
#tr is a html tag
length = len(soup.find_all("tr"))

#start from the back of the data,
#as we want more recent results
counter = length - 10

pos = 0

while check == 0:
    #check the data
    a = soup.find_all("tr")[counter].get_text()
    #convert the data into a string
    s = str(a)
    #split the string
    x = s.split()
    
    #season data comes just before game data
    #end for loop
    if x[0] == "Season":
        check = 1;
        pos = counter

    counter = counter- 1


arr = []
dates = []

for i in range(pos - 30,pos):
    a = soup.find_all("tr")[i].get_text()
    s = str(a)
    x = s.split()
    test = str(x[0])
    
    if test == "2012-13":
        print(test)
        print(x[0], x[3])
        
    arr.append(x[3])
    dates.append(x[0])

xAxis = len(dates)
#########################################################################

# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

width = 1200
height = 600

pygame.init()
DISPLAYSURF = pygame.display.set_mode((width,height))

dataPos = [height-30]
xPosAxis = []
#x axis
x = 20
pos = 0


#y axis
yAxisPoint = height - 30

for i in range (1, 38):
    #pygame.draw.rect(DISPLAYSURF, RED, (ypos, dataPos, 10, 10))
    font = pygame.font.SysFont(None, 16)
    text = str(i)
    img = font.render(text, True, BLUE)
    DISPLAYSURF.blit(img, (6 , yAxisPoint))
    yAxisPoint = yAxisPoint - 15
    dataPos.append(yAxisPoint)
    

for i in range(20,xAxis):
    #pygame.draw.rect(DISPLAYSURF, RED, (pos, 200, 10, 10))
    pos = pos + 100
    xPosAxis.append(pos)
    font = pygame.font.SysFont(None, 16)
    img = font.render(dates[i], True, BLUE)
    DISPLAYSURF.blit(img, ( pos , height - 15))



#drawing the data points
yos = 10
arrLen = len(arr)
Xcounter = 0
for i in range (20, arrLen):
    index = int(arr[i])
    print(index)
    pygame.draw.rect(DISPLAYSURF, RED, (xPosAxis[Xcounter], dataPos[index - 1], 10, 10))
    Xcounter = Xcounter + 1

#x axis
pygame.draw.line(DISPLAYSURF, WHITE, (x,height - 20), (width - 20, height - 20))

#y axis
pygame.draw.line(DISPLAYSURF, WHITE, (x,height-20), (x, 20))




##pygame things
while True:
    pygame.display.update()
    
    for event in pygame.event.get():
        for rectangle in rectangles:
            rectangle.draw()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
	
