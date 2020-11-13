class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        U = len(nums) - 1
        L = 0
        mid = 0
        
        if len(nums) == 0:
            return [-1, -1]
        
        while L <= U:
            mid = (U+L) // 2
            if nums[mid] < target: 
                L = mid + 1
            elif nums[mid] > target:
                U = mid - 1
            else:
                if nums[L] != target:
                    L += 1
                elif nums[U] != target:
                    U -= 1
                elif nums[L] == target and nums[U] == target:
                    return [L, U]
        
        return [-1, -1]
