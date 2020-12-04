class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_arr = []
        
        i = 0
        j = n
        
        while n != 0:
            shuffled_arr.append(nums[i])
            shuffled_arr.append(nums[j])
            
            i += 1
            j += 1
            
            n -= 1
        
        return shuffled_arr
