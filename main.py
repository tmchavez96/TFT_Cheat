#screenshoit imports
import pyautogui
import time

#image handling
import numpy as np
import cv2
import os

#iomage to text
from PIL import Image
import pytesseract
import os

# importing the required module
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from random import seed
from random import randint
seed(2)


#screenshot functions
def getImageName(count):
    path = "C:\\Users\\Taylor Chavez\\Desktop\\developer\\tft\\images\\"
    imgName = "tft" + str(count) +".png"
    return path + imgName

def getImageName2():
    path = "C:\\Users\\Taylor Chavez\\Desktop\\developer\\tft\\images\\curIMG\\"
    imgName = "tft.png"
    return path + imgName


#create sub images function
def analytica():
    # cwd = os.getcwd()
    # next = cwd+  r"\images\curIMG"
    # os.chdir(next)

    img = cv2.imread('tft.png',cv2.IMREAD_COLOR)
    height, width, channels = img.shape
    print(str(height) + " - " + str(width) + " - " + str(channels))
    # test = img[900:1080,475:675];

    x = 1
    x1 = 485
    x2 = 600
    while(x < 6):
        if(x == 5):
            x1 += 5
            x2 += 5
        print("in loop iteration - " + str(x))
        test = img[1040:1065,x1:x2];
        filename = "subImg" + str(x) + ".png"
        newimg = cv2.resize(test,(500,100))
        cv2.imwrite(filename, newimg)
        x1 += 200
        x2 += 200
        x += 1

    # cv2.imshow('image',newimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

#tester
def analytica2(flag):
    # cwd = os.getcwd()
    # next = cwd+  r"\images\curIMG"
    # os.chdir(next)

    if(flag):
        img = cv2.imread('tft43.png',cv2.IMREAD_COLOR)
    else:
        img = cv2.imread('tft50.png',cv2.IMREAD_COLOR)
    height, width, channels = img.shape
    print(str(height) + " - " + str(width) + " - " + str(channels))
    # test = img[900:1080,475:675];

    x = 1
    x1 = 485
    x2 = 600
    while(x < 6):
        if(x == 5):
            x1 += 5
            x2 += 5
        print("in loop iteration - " + str(x))
        test = img[1040:1065,x1:x2];
        filename = "subImg" + str(x) + ".png"
        newimg = cv2.resize(test,(500,100))
        cv2.imwrite(filename, newimg)
        x1 += 200
        x2 += 200
        x += 1

    # cv2.imshow('image',newimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

#graophing functions
x=[]
y=[]

def randomizeList(cList):
    for key in cList:
        value = randint(0, 1200)
        cList[key] = value
#seeTopTen(charList)
#return the pair of key with hghest value pair
def getHighest(cList):
    index = 0
    i1 = -1
    k1 = ""
    v1 = -1;
    for key in cList:
        if(index == 0):
            k1 = key
        if(cList[key] > v1):
            i1 = index
            k1 = key
            v1 = cList[key]
        index += 1
    cList.pop(k1)
    print("popped - " + k1)
    return k1,v1

#get the x amount of most common cards
def getHighestList(x,cList):
    rv = {}
    tempList = cList.copy()
    #randomizeList(tempList)
    while(x > 0):
        k1,v1 = getHighest(tempList)
        rv[k1] = v1
        x -= 1
    print("list lengtrht - " + str(len(rv)))
    return rv

def seeTopTen(cList):
    list = getHighestList(15,cList)
    drawList(list)

def drawList(cList):
    for key in cList:
        print("iterating draw list")
        keyval = key[:4]
        x.append(keyval)
        y.append(cList[key])
    # plotting the points
    plt.bar(x, y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()

#returns list of reconized names
def machineLearn():
    x = 1;
    rv = []
    while x < 6:
        filename = "subImg" + str(x) + ".png"
        im = Image.open(filename)
        test = pytesseract.image_to_string(im,lang="eng")
        print("***************")
        print("for image " + str(x))
        print(test)
        rv.append(test)
        x+=1
    return rv

def getCharList():
    charList = {
        'Ivern':0,
        "Kog'Maw":0,
        "MAOKAI":0,
        "Nasue":0,
        "Renekton":0,
        "Taliyah":0,
        "Vladimir":0,
        "Warwick":0,
        "Zyra":0,
        "Vayne":0,
        "Diana":0,
        "Ornn":0,
        "Braum":0,
        "Jax":0,
        "Leblanc":0,
        "Rek'Sai":0,
        "Syndra":0,
        "Thresh":0,
        "Varus":0,
        "Yasuo":0,
        "Malzahar":0,
        "Neeko":0,
        "Skarner":0,
        "Volibear":0,
        "Aatrox":0,
        "Azir":0,
        "Dr. Mundo":0,
        "Ezreal":0,
        "Kindred":0,
        "Nautilus":0,
        "Nocturne":0,
        "Veigar":0,
        "Sivir":0,
        "Sion":0,
        "Soraka":0,
        "Qiyana":0,
        "Ashe":0,
        "Annie":0,
        "Janna":0,
        "Kha'Zix":0,
        "Malphite":0,
        "Twitch":0,
        "Brand":0,
        "Yorick":0,
        "Olaf":0,
        "Nami":0,
        "Singed":0,
        "Taric":0,
        "Zed":0,
        "Master Yi":0,
        "Lux":0,
    }
    return charList

#return false if either strin is null, return true otherwise
#assume tesseratc returns string len 0 as opposed to null
def checkNull(s1,s2):
    if(len(s1) < 3):
        return False
    elif(len(s2) < 3):
        return False
    else:
        return True



#return 0 if same, 1 if dif
def compareList(prev,cur):
    index = 0
    simArr =[]
    for c1 in cur:
        c2 = prev[index]
        if c1 == c2 or len(c2) < 3:
            #if checkNull(c1,c2):
            simArr.append(True)
        else:
            simArr.append(False)
        index += 1
    for t in simArr:
        if(t == False):
            return True
    return False



def incrementDict(cList,curChars,prev):
    if compareList(curChars,prev):
        print("passed comapre")
        for char in curChars:
            for key in cList:
                if(key == char):
                    cList[key] += 1
                    break
    else:
        print("was same as last")

def dictToString(dict):
    rv = ""
    for key in dict:
        rv += key
        rv += ":"
        rv += str(dict[key])
        rv += "\n"
    return rv

def writeDict(cList):
    f = open("dict.txt", "w")
    f.write(dictToString(cList))
    f.close()

def readDict():
    rv = {}
    f = open("dict.txt", "r")
    for x in f:
        i = word.find('for')
        key = x[:i]
        val = x[i+1:]
        rv[key] = val
    return rv

def main():
    #requires user input to break
    cwd = os.getcwd()
    next = cwd+  r"\images\curIMG"
    os.chdir(next)
    cList = getCharList()
    prev = machineLearn()
    ix = 0
    while(True):
        try:
            pyautogui.screenshot(getImageName2())
            print("screenshot shot succsesful")
        except:
            break;
            print("something went wrong in screenshot")
        print("%%%%% got screenshot, creating subimages")
        if(ix %2 == 0):
            analytica2(True)
        else:
            analytica2(False)
        curChars = machineLearn()
        incrementDict(cList,curChars,prev)
        figure(num=None, figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')
        #seeTopTen(cList)
        writeDict(cList)
        prev = curChars
        time.sleep(3)
        ix += 1

main()
