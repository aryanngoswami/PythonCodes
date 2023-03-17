def rotateArr(arr,d):
    a=arr[-1::-1]
    a1=[]
    a2=[]
    for i in range(len(a)-d):
        a1.append(a[i])
    for j in range(len(a1),len(arr)):
        a2.append(a[j])
    a1=a1[-1::-1]
    a2=a2[-1::-1]
    return a1+a2
arr=[1,3,6,11,12,17,22,26,30,33,38]
d=7
arr=rotateArr(arr,d)
print(arr)