arr=[7, 3, 5, 3, 1, 7]

for i in range(1, len(arr)):
    key=arr[i]
    j=i-1

    while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key

print(arr)

# selection sorts duplikātus ar vietām nemaina