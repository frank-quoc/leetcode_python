class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ind_dict = {}
        for i in range(len(nums)):
            if nums[i] in ind_dict:
                if i - ind_dict[nums[i]] <= k:
                    return True
            ind_dict[nums[i]] = i
        return False
