'''
Q : Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
'''
class Solution:
    '''
    Main class for the solution
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Main function
        **Input:** nums = [2,7,11,15], target = 9
        **Output:** [0,1]
        **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].
        '''
        hash_map = {}
        for idx, val in enumerate(nums):
            n_val = target - val
            if n_val in hash_map:
                return [hash_map[n_val], idx]
            else:
                hash_map[val] = idx
