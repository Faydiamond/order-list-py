list = [50,10,2,40,12,5,1,22,12,15,35,19]
x = len (list)
print ("pos", x)
for l in range(x):
    for ch in range(0, x-l- 1):
        if (list[ch] > list[ch+1]):
            list[ch], list[ch+1] = list[ch+1] , list[ch]
print (list)