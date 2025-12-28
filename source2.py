render = []
    
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
    one = True
    two = True
    three = True
    
    while True:
        if one and not two and not three:
            num = "1"
        elif two and not one and not three:
            num = "2"
        elif three and not one and not two:
            num = "3"
        elif two and three and not one:
            num = input("Input the block (2,3) that you want to place: ")
        elif one and three and not two:
            num = input("Input the block (1,3) that you want to place: ")
        elif one and two and not three:
            num = input("Input the block (1,2) that you want to place: ")
        elif one and two and three:
            num = input("Input the block (1,2,3) that you want to place: ")
            
        x = input("Input the x coordinate (0-7) where you want to place the block: ")
        y = input("Input the y coordinate (0-7) where you want to place the block: ")
        
        # Assign blocks to their respective number
        block = None
        if num == "1":
            block = first.shape
            one = False
        elif num == "2":
            block = second.shape
            two = False
        elif num == "3":
            block  = third.shape
            three = False
        else:
            print("Failed to assign block")
            
        if (1<=int(num)<=3) and (0<=int(x)<=7) and (0<=int(y)<=7) and (check(canvas,block,int(x),int(y))):
            return [canvas,block,int(x),int(y),num]
        else:
            print("The block you tried to place is not placable in that location, please try again")
        
def check(canvas,item,x,y):
    try:
        for i in range(len(item)):
            for j in range(len(item[i])):
                if canvas[y+i][x+j] != 0 and item[i][j] != 0:
                    return False
    except:
        return False
    return True
    
    

