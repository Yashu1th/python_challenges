nums=[1,2,3,4,5,6,7] 
k=3
def rotate(nums,k):
  n=len(nums)
  nums[:]=nums[n-k:]+nums[:n-k]
  return nums
rotate(nums,k)
print(nums)
