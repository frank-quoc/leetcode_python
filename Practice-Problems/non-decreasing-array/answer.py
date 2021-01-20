class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums = [float('-inf')] + nums + [float('inf')]
        i = 1
        changed = False # Flag to see if we changed a number already
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]: # if current number > next number
                if changed: # if we have already changed a number
                    return False
                else:
                    if nums[i] <= nums[i+2]: # if current number <= 2 numbers down
                        nums[i+1] = nums[i]
                    else: # if it's current number is greater than 2 numbers down
                        nums[i] = nums[i-1]
                        i -= 1
                    changed = True
            i += 1
        return True
