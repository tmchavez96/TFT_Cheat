from tkinter import *
# importing the required module
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from random import seed
from random import randint
import os
seed(2)
figure(num=None, figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')


cwd = os.getcwd()
next = cwd+  r"\images\curIMG"
os.chdir(next)

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
    "Kindred":2,
    "Nautilus":0,
    "Nocturne":0,
    "Veigar":0,
    "Sivir":3,
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

def readDict():
    rv = {}
    f = open("dict.txt", "r")
    for x in f:
        i = x.find(':')
        key = x[:i]
        val = x[i+1:]
        rv[key] = int(val)
    return rv

def graphMe():
    cList = readDict()
    seeTopTen(cList)



root = Tk()

theFrame = Frame(root)
theFrame.pack()

curwidth=400
curheight=200
w = Canvas(root, width = curwidth, height = curheight)
w.pack()

frame = Frame(root,bg = "grey")
frame.place(relwidth = 3,relheight = 1.0)

exitbutton = Button(frame, text="Quit", bg="red",command=root.destroy)
exitbutton.grid(row=0,column=0)

button = Button(frame,text="See Top Ten",bg="green",state="normal",command=graphMe)
button.grid(row=4,column=0)

root.mainloop()
