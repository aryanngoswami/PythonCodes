# arr=[5,5,5,5]
# arr=list(set(arr))
# l=-1
# s=-1
# for i in range(len(arr)):
#     if arr[i]>l:
#         l=arr[i]
# arr.remove(l)
# for j in range(len(arr)):
#     if arr[j]>s:
#         s=arr[j]
# print("secondlargest",s)

arr=[2,6,1,9,8,9,7]
l=-1
s=-1
for i in range(len(arr)):
    if arr[i]>l:
        l=arr[i]
for j in range(len(arr)):
    if arr[j]>s and arr[j]<l:
        s=arr[j]

print(s)


