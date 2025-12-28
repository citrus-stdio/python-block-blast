from funcs import *
import random

class block:
    def __init__ (self, s,w,l):
        self.shape = s
        self.width = w
        self.length = l
        
lblock1 = block([[1,0],[1,0],[1,1]],2,3)
lblock2 = block([[0,1],[0,1],[1,1]],2,3)
lblock3 = block([[1,1],[1,0],[1,0]],2,3)
lblock4 = block([[1,1],[0,1],[0,1]],2,3)
smallsquare = block([[1,1],[1,1]],2,2)
bigsquare = block([[1,1,1],[1,1,1],[1,1,1]],3,3)
corner1 = block([[1,0,0],[1,0,0],[1,1,1]],3,3)
corner2 = block([[0,0,1],[0,0,1],[1,1,1]],3,3)
corner3 = block([[1,1,1],[1,0,0],[1,0,0]],3,3)
corner4 = block([[1,1,1],[0,0,1],[0,0,1]],3,3)
zig1 = block([[1,1,0],[0,1,1]],3,2)
zig2 = block([[0,1,1],[1,1,0]],3,2)
zag1 = block([[0,1],[1,1],[1,0]],2,3)
zag2 = block([[1,0],[1,1],[0,1]],2,3)
line1 = block([[1],[1],[1],[1]],1,4)
line2 = block([[1,1,1,1]],4,1)
line3 = block([[1],[1],[1],[1],[1]],1,5)
line4 = block([[1,1,1,1,1]],5,1)
tblock1 = block([[1,1,1],[0,1,0]],3,2)
tblock2 = block([[0,1],[1,1],[0,1]],2,3)
tblock3 = block([[0,1,0],[1,1,1]],3,2)
tblock4 = block([[1,0],[1,1],[1,0]],2,3)

board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
xstrip = [["0","1","2","3","4","5","6","7"]]
ystrip = [["0"],["1"],["2"],["3"],["4"],["5"],["6"],["7"]]
blocks = [lblock1,lblock2,lblock3,lblock4,smallsquare,bigsquare,corner1,corner2,corner3,corner4,zig1,zig2,zag1,zag2,line1,line2,line3,line4,tblock1,tblock2,tblock3,tblock4]
blocklistx = 12
blocklisty = 5

render = fillRender(30,10)
place(render,xstrip,1,0)
place(render,ystrip,0,1)
#while True:

# Behold the texturizer
texturize(blocks,"x")
# Block selection
block1 = random.choice(blocks)
block2 = random.choice(blocks)
block3 = random.choice(blocks)
# Put block choice on the screen
place(render,block1.shape,blocklistx,blocklisty)
place(render,[[","]],blocklistx+1+block1.width,blocklisty)
place(render,[["1"]],blocklistx,blocklisty-2)
place(render,block2.shape,blocklistx+3+block1.width,blocklisty)
place(render,[[","]],blocklistx+4+block1.width+block2.width,blocklisty)
place(render,[["2"]],blocklistx+4+block1.width,blocklisty-2)
place(render,block3.shape,blocklistx+6+block1.width+block2.width,blocklisty)
place(render,[["3"]],blocklistx+6+block1.width+block2.width,blocklisty-2)

# Display board so that player can see before placing blocks :)
place(render,board,1,1)
displayRender()

for i in range(0,3):
    # Get player input
    playerInput = getPlayerInput(board,block1,block2,block3)
    place(playerInput[0],playerInput[1],playerInput[2],playerInput[3])
    # Clear block that is used from screen
    if playerInput[4] == "1":
        fill(render,blocklistx,blocklisty,blocklistx+block1.width,blocklisty+block1.length)
    elif playerInput[4] == "2":
        fill(render,blocklistx+3+block1.width,blocklisty,blocklistx+3+block1.width+block2.width,blocklisty+block2.length)
    elif playerInput[4] == "3":
        fill(render,blocklistx+6+block1.width+block2.width,blocklisty,blocklistx+6+block3.width+block2.width+block1.width,blocklisty+block3.length)
    
    # Place board on render again and display the render
    place(render,board,1,1)
    displayRender()
    
    
    
    #if input("press 0 to continue: ") != str(0):
        #break

