
"""
Dragon Curve SVG Creator
By potteryclay
Directly inspired by and using code from Gainsboroow 
(Github : https://github.com/Gainsboroow
Github Repository : https://github.com/Gainsboroow/Dragon-Curve)

This is an extension of Gainsboroow's Dragon Curve Visualiser that generates
a set of dragon curve svg's.
"""

from svg_turtle import SvgTurtle
from copy import deepcopy

nbFolds = int(input("Starting number of folds : "))

t=SvgTurtle((1000*nbFolds),(1000*nbFolds))
lineweight=10
leng = 4*lineweight

t.width(lineweight)

def drawing(folds,a,length):
    for z in range(folds):
        copie = deepcopy(a)
        for i in copie[::-1]:
            a.append(1-i)
        a.insert(len(a)//2, 0)

    t.down()

    t.forward(length)
    for i in a:
        if i:
            t.right(90)
        else:
            t.left(90)
        t.forward(length)

arr = []

it = int(input("Number of iterations: "))
arr2 = []

for j in range(it):
    arr2.append(j)

for k in range(len(arr2)):
    k=int(k)
    f = open("%dragon.txt" % k,'x')
    f.write("hiiii" + k)
    f.close
    nbFolds=nbFolds+k
    drawing(nbFolds,arr,leng)
    t.save_as(arr[k]+"dragon1.svg")

#t.save_as('dragon1.svg')
print('Done.')
