#Insertion Sort
j = 1 #It starts comparing the array's second position (j=1) with the first position (j=0) 
array = [5,4,3,2,7,1,]

for j in range (1, len(array)):
    key = array[j]
    i = j -1
    while (i>=0 and array[i]>key):
        array[i+1] = array[i]
        i = i -1
    array[i+1] = key

print (array)
