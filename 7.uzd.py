arr=[("Latvia", 300), ("Lithuania", 100), ("Latvia", 200)]

for j in range(len(arr) - 1):
    vertiba = False

    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            vertiba = True
    
    if not vertiba:
        break

print(arr)