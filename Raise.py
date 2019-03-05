import random

def creatArray(x,y):
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(0,100)) 
    return array

def creatArray1(x1,y1):
    array1 = []
    for i in range(a):
        if i == x1:
            i = i-1
            for m in range(i,a):
                if i != x1:
                    array1.append([])
                    for j in range(b):
                        if j != y1:
                            break
                    break
        else:    
            array1.append([])
            for j in range(b):
                if j != y1:
                    array1[i].append(c[i][j])
    return array1

a = 10
b = 10
c = creatArray(a,b)
print (c)
t = 2
u = 3
e = creatArray1(t,u)
print (e)


