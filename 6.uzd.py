arr=[(101, 85), (102, 70), (103, 95)]

for j in range(len(arr)-1):
    vertiba=False

    for i in range(len(arr)-1):
        if (arr[i][1]<arr[i+1][1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            vertiba = True
    
    if not vertiba:
        break


print(arr)