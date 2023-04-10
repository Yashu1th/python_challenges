
def removeDuplicate(arr):
  x=1
  for i in range(len(arr)-1):
    if(arr[i]!=arr[i+1]):
      arr[x]=arr[i+1]
      x+=1
  return x

arr=[1,1,2,2,3,3,4,4,5,5,6,6,6,7,7]
removeDuplicate(arr)
