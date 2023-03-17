def rotateArr(arr,d):
    i=1
    while i<=d:
        for j in range(len(arr)-1):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
        i+=1
    return arr
arr=[1,2,3,4,5,6,7]
d=2
arr=rotateArr(arr,d)
print(arr)