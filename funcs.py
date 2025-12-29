render = []

# errors!!
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
            if item[i][j] != 0 and item[i][j][0] != "[":
                canvas[y+i][x+j] = f"[{item[i][j]}]"
            elif item[i][j] != 0:
                canvas[y+i][x+j] = f"{item[i][j]}"
                
def texturize(list,texture):
    for i in range(len(list)):
        for j in range(len(list[i].shape)):
            for k in range(len(list[i].shape[j])):
                if list[i].shape[j][k] == 1:
                    list[i].shape[j][k] = texture
    
    return list

def getPlayerInput(canvas,first,second,third):
    blocks = {
        "1" : [first.shape,True],
        "2" : [second.shape,True],
        "3" : [third.shape,True]
    }

    # creates an array in which the number is only displayed if the number's corresponding boolean in the blocks dictionary is true
    available = [num for num, (_,avail) in blocks.items() if avail]
    print(available)

    # let the player choose a block
    if len(available) == 1:
        num = available[0]
    else:
        num = input(f"Choose a block : {tuple(available)}")

    # check availability
    if num not in available :
        raise InvalidBlockChoice(f"Block not available, please choose from the available blocks {tuple(available)}")

    block = blocks[num][0]
    blocks[num][1] = False

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
    return canvas, block, x, y,num

def check(canvas,item,x,y):
    try:
        for i in range(len(item)):
            for j in range(len(item[i])):
                if canvas[y+i][x+j] != 0 and item[i][j] != 0:
                    return False
    except:
        return False
    return True
    
    

