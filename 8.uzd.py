arr=[5, -2, 8, -5, 10, 0, -10]

for j in range(len(arr)-1):
    vertiba=False

    for i in range(len(arr)-1):
        if (arr[i]>arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            vertiba = True
    
    if not vertiba:
        break


for k in range(len(arr)-1):
    if(arr[k]==0):
        arr[k], arr[k+1] = arr[k+1], arr[k]

print(arr)