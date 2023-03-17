arr=[-2,-13,-4,-1,-3,-6,-28]
max=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)
