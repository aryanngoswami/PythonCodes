def pushZerosAtEnd(arr) :
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]!=0 and arr[j]==0:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print(arr)
arr=[2,0,0,1,3,0,0]
pushZerosAtEnd(arr)
