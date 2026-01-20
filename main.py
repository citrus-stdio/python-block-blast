from funcs import *
import random

class block:
    def __init__ (self, s,w,l):
        self.shape = s
        self.width = w
        self.length = l


score = 0
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
quit_all = False

board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
xstrip = [["0","1","2","3","4","5","6","7"]]
ystrip = [["0"],["1"],["2"],["3"],["4"],["5"],["6"],["7"]]
blocklist = [lblock1,lblock2,lblock3,lblock4,smallsquare,bigsquare,corner1,corner2,corner3,corner4,zig1,zig2,zag1,zag2,line1,line2,line3,line4,tblock1,tblock2,tblock3,tblock4]
blocklistx = 12
blocklisty = 5
scoreboard = [["S","C","O","R","E",":"," ",str(score)]]

render = fillRender(30,10)
place(render,xstrip,1,0)
place(render,ystrip,0,1)
place(render,scoreboard,14,1)

# Behold the texturizer
blocklist = texturize(blocklist, "x")

while True:
    # Block selection
    block1 = random.choice(blocklist)
    block2 = random.choice(blocklist)
    block3 = random.choice(blocklist)
    # block dictionary!!
    blocks = {
        "1": [block1.shape, True],
        "2": [block2.shape, True],
        "3": [block3.shape, True]
    }

    # reset render
    render = fillRender(30, 10)
    place(render, xstrip, 1, 0)
    place(render, ystrip, 0, 1)
    place(render, scoreboard, 14, 1)

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

        while True:
            try:
                playerInput = getPlayerInput(board,blocks)
                break
            except(Exception) as e:
                # specified instruction error
                print(e)

        # place block on the board
        place(playerInput[0],playerInput[1],playerInput[2],playerInput[3])
        # Clear block that is used from screen
        clearChoice(playerInput[4],block1,block2,block3,blocklistx,blocklisty)
        # clear lines
        cleared = clear(board)
        board = cleared[0]
        score += cleared[1]
        # print the scoreboard
        scoreboard = [["S", "C", "O", "R", "E", ":", " ", str(score)]]
        place(render, scoreboard, 14, 1)

        # reset render
        fill(render,1,1,9,9)

        # Place board on render again and display the render
        place(render,board,1,1)
        displayRender()

        # make the block just chosen unavailable
        blocks[str(playerInput[4])][1] = False

        # check for lose state
        if i != 2:
            if loseState(board,blocks):
                loseScreen(score)
                quit_all = True


        if quit_all:
            break
    if quit_all:
        break

print("Thanks for playing o7")

