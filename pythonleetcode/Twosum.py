from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     prevEl = {} # val and index

     for i, n in enumerate(nums):
         diff = target - n
         if diff in prevEl:
            return [prevEl[diff], i]
         prevEl[n] = i
     return []
        

nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the target sum: "))

# Creating an object of Solution class
solution = Solution()
result = solution.twoSum(nums, target)

# Printing the result
print("Indices:", result)