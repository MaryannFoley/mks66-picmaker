import random

WIDTH=1000
HEIGHT=1000
MAXVAL=255

retstr=""

def header():
    top="P3 \n"
    size=str(HEIGHT) + " "+str(WIDTH)+"\n"
    max=str(MAXVAL)+"/n"
    retstr=top+size+max
    return retstr

def main():
    file=open("image.ppm","w")
    file.write(header())
    file.write(makeDesign())
    file.close()

WHITE="254 255 252"
BLACK="0 0 0"
RED="255 12 5"
BLUE="30 62 219"
YELLOW="255 251 17"

colorList=["255 102 0","255 255 0","51 204 51","0 204 153","0 102 255","153 51 255","255 51 204","255 0 0","255 255 255", "102 255 51"]

def makeDesign():
    ## trying to make a mondrian style painting, it really just makes stripes
    # black border (1/100 of width and height)
    # start white/color after border
    # generate a random nnum, if it equals something then stop using the color to the left, use black
    # make a line of the same 1/100 width
    # next row: check line above, generate a random num, if it equals something then stop using the color on top, use black
    arr=[]#2d array
    for row in range(HEIGHT):
        tempRowList=[]
        for col in range(WIDTH):
            if row < int(HEIGHT/100) or row >= HEIGHT-int(HEIGHT/100):
                tempRowList.append(BLACK)
            elif col < int(WIDTH/100) or col >= WIDTH-int(WIDTH/100):
                tempRowList.append(BLACK)
            else:
                #count black to left and above
                ctA=0
                for i in range(int(HEIGHT/100)):
                    if arr[row-1-i][col] == BLACK:
                        ctA+=1
                    else:
                        break
                ctL=0
                for i in range(int(WIDTH/100)):
                    #print("["+str(row)+","+str(col-i-1)+"]")
                    if tempRowList[col-1-i] == BLACK:
                        ctL+=1
                    else:
                        break
                if ctA == 0 or ctL==0: #means it's touching some other color
                    if random.randint(0,100)==14:
                        tempRowList.append(BLACK)
                    elif arr[row-1][col] != BLACK:
                        tempRowList.append(arr[row-1][col])
                    else:
                        tempRowList.append(tempRowList[col-1])
                elif ctA < int(HEIGHT/100) or ctL < int(HEIGHT/100):
                    tempRowList.append(BLACK)
                else: #start of a new block
                    #randC=random.randint(0,10)
                    #if randC == 4:
                    #    tempRowList.append(RED)
                    #elif randC == 6:
                    #    tempRowList.append(BLUE)
                    #elif randC == 8:
                    #    tempRowList.append(YELLOW)
                    #else:
                    #    tempRowList.append(WHITE)
                    tempRowList.append(random.choice(colorList))
        arr.append(tempRowList)
    mkStr=""
    for row in arr:
        for col in row:
            mkStr+=col+" "
        mkStr+="\n"
    return mkStr
main()
