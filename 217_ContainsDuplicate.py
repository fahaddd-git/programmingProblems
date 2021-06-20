# ID: 217
# URL: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(nums: list[int]):
        """
        algorithm:
            - compare the length of the list to the length of the list as a set
            - return False if they are equal
            - return True if they are unequal
        """
        return len(set(nums))!=len(nums)


