class Solution:
    # Dynamic Approach
#     def maxSubArray(self, nums: List[int]) -> int:
#         sums = [0] * len(nums)
#         sums[0] = nums[0]
#         for i in range(1, len(nums)):
#             if sums[i-1] + nums[i] > nums[i]:
#                 sums[i] = sums[i-1] + nums[i]
#             else:
#                 sums[i] = nums[i]
                
#         return max(sums)
    
    # Divide & Conquer (someone else's solution)  
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        
        mid = l // 2
        
        left = self.maxSubArray(nums[:mid])
        right = self.maxSubArray(nums[mid:])
        center = self.maxCenter(nums, mid)
        
        return max(left, right, center)

    def maxCenter(self, nums, mid):
        chk_l_sum = chk_r_sum = 0
        l_sum = r_sum = float('-inf')
        
        for i in range(mid-1, -1, -1):
            chk_l_sum += nums[i]
            l_sum = max(l_sum, chk_l_sum)

        for j in range(mid, len(nums)):
            chk_r_sum += nums[j]
            r_sum = max(r_sum, chk_r_sum)
            
        return l_sum + r_sum
