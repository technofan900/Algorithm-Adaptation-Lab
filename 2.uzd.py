arr2=[5, 1, 4, 2, 8]
count=0
for j in range(len(arr2)-1):
    vertiba=False

    for i in range(len(arr2)-1):
        if (arr2[i]<arr2[i+1]):
            arr2[i], arr2[i+1] = arr2[i+1], arr2[i]
            vertiba = True
            count+=1
    
    if not vertiba:
        break
print(arr2)
print(count)