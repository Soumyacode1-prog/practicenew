# Store frequency of elements.
nums=[1,5,1,1,5,2,3,2,7,2]
class Solution:
    def freq(self,nums):

        freq_map=dict()
        for i in range(0,len(nums)):
            if nums[i] in freq_map:
                freq_map[nums[i]]+=1

            else:
                freq_map[nums[i]]=1  

        print(freq_map)
obj=Solution()
# obj.freq(nums)
print(obj.freq(nums))              