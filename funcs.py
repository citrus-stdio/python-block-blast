render = []

# errors!!!
class InvalidBlockChoice(Exception) : pass
class InvalidCoordinate(Exception) : pass
class PlacementError(Exception) : pass

def display(item) :
    for arr in item:
        print(str(arr))

def fillRender(x,y) :
    global render
    render = []
    for i in range(0,y+1):
        render.append([])
        for j in range(0,x+1):
            render[i].append("   ")
        render[i].append("\n")
    return render
    
def fill(canvas,x1,y1,x2,y2):
    for i in range(y1,y2):
        for j in range(x1,x2):
            canvas[i][j] = "   "


def displayRender():
    global render
    for i in range(len(render)):
        for j in render[i]:
            print(j,end="")
   
def place(canvas,item,x,y) :
    for i in range(len(item)):
        for j in range(len(item[i])):
            cell = item[i][j]

            if cell == 0:
                continue

            if isinstance(cell,str) and not cell.startswith("["):
                canvas[y+i][x+j] = f"[{cell}]"
            else:
                canvas[y+i][x+j] = str(cell)
                
def texturize(list,texture):
    for i in range(len(list)):
        for j in range(len(list[i].shape)):
            for k in range(len(list[i].shape[j])):
                if list[i].shape[j][k] == 1:
                    list[i].shape[j][k] = texture
    
    return list

def getPlayerInput(canvas,blocks):

    # creates an array in which the number is only displayed if the number's corresponding boolean in the blocks dictionary is true
    available = [num for num, (_,avail) in blocks.items() if avail]

    # let the player choose a block
    if len(available) == 1:
        num = available[0]
    else:
        num = input(f"Choose a block : {tuple(available)}")

    # check availability
    if num not in available :
        raise InvalidBlockChoice(f"Block not available, please choose from the available blocks {tuple(available)}")

    block = blocks[num][0]

    x = input("Input the x coordinate (0-7) where you want to place the block: ")
    y = input("Input the y coordinate (0-7) where you want to place the block: ")

    # check if inputs are integers
    try:
        x = int(x)
        y = int(y)
    except:
        raise InvalidCoordinate("Coordinates must be an integer")

    # check if inputs are within bounds

    if not (0<=x<=7 and 0<=y<=7):
        raise InvalidCoordinate(f"Coordinates must be between 0 and 7, got ({x},{y})")

    # check if block is placeable

    if check(canvas,block,int(x),int(y)) == False:
        raise PlacementError(f"Block {num} cannot be placed at ({x},{y})")

    # success!
    return canvas, block, x, y, num

def check(canvas,item,x,y):
    try:
        for i in range(len(item)):
            for j in range(len(item[i])):
                if canvas[y+i][x+j] != 0 and item[i][j] != 0:
                    return False
    except:
        return False
    return True

def clearChoice(num, first, second, third, x, y):
    # here, x and y represent the present coordinates of the block list

    blocks = {
        "1": first,
        "2": second,
        "3": third
    }

    # offset to make things go into actual place, i forgot why it doesn't work without, oh well
    offset = 0

    for i in range(1,int(num)):
        offset += blocks[str(i)].width

    offset += (int(num)-1)*3

    xAligned = x+offset

    fill(render, xAligned, y, xAligned + blocks[str(num)].width, y + blocks[str(num)].length)

def clear(canvas):
    counter = 0
    points = 0
    combo = 0

    clearables = {
        "x" : [0,0,0,0,0,0,0,0],
        "y" : [0,0,0,0,0,0,0,0]
    }

    # check for horizontal clearings

    for i in range(0,len(canvas)):
        for j in range(0,len(canvas[i])):
            if canvas[i][j] != 0:
                counter += 1

        if counter >= len(canvas[i]):
            clearables["y"][i] = 1

        # reset counter after iteration
        counter = 0

    # check for vertical clearings

    for j in range(0,len(canvas[0])):
        for i in range(0,len(canvas)):
            if canvas[i][j] != 0:
                counter += 1

        if counter >= len(canvas[i]):
            clearables["x"][j] = 1

        # reset counter after iteration
        counter = 0

    # clear horizontally

    for i in range(0,len(canvas)):
        if clearables["y"][i] == 1:
            for j in range(0,len(canvas[i])):
                canvas[i][j] = 0


    # clear vertically

    for j in range(0,len(canvas[0])):
        if clearables["x"][j] == 1:
            for i in range(0,len(canvas)):
                canvas[i][j] = 0

    for i in range(0,len(clearables["x"])):
        combo += clearables["x"][i]
        combo += clearables["y"][i]


    points = 20 * combo * combo

    return canvas, points

def loseState(canvas,available):
    for i in range(len(available)):
        block,avail = available[str(i+1)]

        if not avail:
            continue

        for y in range(len(canvas)):
            for x in range(len(canvas[y])):
                if check(canvas,block,x,y):
                    return False # possible block placement

    return True # lose state

def loseScreen(score):
    # reset render
    render = fillRender(30, 10)
    place(render,[["Y","O","U"," ","L","O","S","T","!"]],5,5)
    place(render, [["H", "I", "G", "H", "S", "C", "O", "R", "E",":",f"[{score}]"]], 5, 6)
    place(render, [["P", "L", "A", "Y", " ", "A", "G", "A", "I", "N","?"]], 5, 7)
    displayRender()


