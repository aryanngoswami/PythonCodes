def Merge(a1,a2):
    arr=[]
    i,j=0,0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            arr.append(a1[i])
            i+=1
        else:
            arr.append(a2[j])
            j+=1
    while i<len(a1):
        arr.append(a1[i])
        i+=1
    while j<len(a2):
        arr.append(a2[j])
        j+=1
    return arr
    


a1=[1,3,4,7,11]
a2=[2,4,6,13]
MargeArr=Merge(a1,a2)
print(MargeArr)