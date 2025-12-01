arr2=[1,5,3,0,-1,5,2,7]

for j in range(len(arr2)-1):
    vertiba=False

    for i in range(len(arr2)-1):
        if (arr2[i]<arr2[i+1]):
            arr2[i], arr2[i+1] = arr2[i+1], arr2[i]
            vertiba = True
    
    if not vertiba:
        break

print(arr2)