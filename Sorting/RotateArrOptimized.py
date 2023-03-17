def rotateArr(arr,d):
    a=arr[0:d]
    for i in range(len(arr)-d):
        arr[i]=arr[i+d]
    k=0
    for j in range(len(arr)-d,len(arr)):
        arr[j]=a[k]
        k+=1
    return arr
arr=[1,2,3,4,5,6,7]
d=2
arr=rotateArr(arr,d)
print(arr)