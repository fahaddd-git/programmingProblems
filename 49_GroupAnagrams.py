# ID: 49
# URL: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Description: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: list[str]):
        """
        algorithm:
        - create a dictionary  which will follow {sorted_item:[unsorted_item]}
        - iterate through strs
            - sort an item
            - if sorted item not in dict, add it as a value in a list with unsorted item as key
            - otherwise if in dictionary already append the unsorted item to the values
        - return list of dictionary values
        """

        strings_dict = {}
        # iterate through strs
        for index, unsorted_item in enumerate(strs):
            # sort an element
            sorted_item = "".join(sorted(unsorted_item))
            # if the sorted element already in the dictionary, append the unsorted element to the list of values
            if sorted_item in strings_dict:
                strings_dict[sorted_item].append(unsorted_item)
            # otherwise add the sorted item as a key and the unsorted item as a list as the values
            else:
                strings_dict[sorted_item]=[unsorted_item]
        # return values from dict
        return [i for i in strings_dict.values()]