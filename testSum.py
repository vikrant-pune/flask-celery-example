"""

https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for n in range(0, len(nums)):
            for j in range(n+1, len(nums)):
                # index_in = index_out + 1
                if nums[n] + nums[j]  == target:
                    return [n, j]
        return []




# class testMe:
def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5

def test_twoSum():
    s = Solution()

    assert s.twoSum(nums=[2,7,11,15], target= 9) == [0,1]

def test_twoSum2():
    s = Solution()
    with pytest.raises(TypeError):
        s.twoSum(nums=2, target= 9)



def test_twoSum3():
    s = Solution()

    assert s.twoSum(nums=[3, 2, 4], target= 6) == [1, 2]

#[3,3], target = 6
# Output: [0,1]



def test_twoSum4():
    s = Solution()

    assert s.twoSum(nums=[3, 3], target= 6) == [0, 1]


def test_twoSum5():
    s = Solution()
    assert s.twoSum(nums=[3, 3], target= 7) == []

def test_twoSum6():
    s = Solution()
    assert s.twoSum(nums=[3, 2, 3], target= 6) == [0,2]


#
# if __name__ == '__main__':
#     Solution.twoSum([2,7,11,15], target = 9)
