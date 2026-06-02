l = [ 4, 5, 3, 2, 5 ]
for i in l:
    print(l.index(i),"->",i)

#------------Enumerate----------------- used for iterating over list----------
print(enumerate(l))

print(list(enumerate(l,start=1)))   #----ADAVATAGE is take index you want------


for ind, val in enumerate(l):
    print(f"{ind} -> {val}")


l2 = l
print(l2)

l.append(50)

l2 = l.copy()
print(l2)

#change the value of 100

l1=[ 50, 51, 56, [ 100, 101], 78]
l2 = l1.copy()
l1[4]=56



print(l1)
print(l2)

l1[3][0]=50
print(l1)
print(l2)