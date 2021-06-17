# ID: 125
# URL: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Description: Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        - ignore case, only letters
        - same forward and backwards
            -characters same until middle of word
        
        example 4 letter length word:
            "abba"
        
        example 5 letter length word
            "acdca"
            
        middle letter won't matter
        
        algorithm:
        - create a list of valid characters
        - iterate through the string (in lower case) and create a new string with only valid letters (in lower case)
        - if new_string length is 0 or 1 return True
        - create two pointers starting at each end of the new string
        - compare the two pointers, if values not equal return false else continue
        - once the index of left pointer is greater than right pointer return True since all values have been checked
        """

        # check if input string is length 1 and therefore a palindrome
        if len(s)==1:
            return True
        
        # list of valid alphanumeric characters
        valid_characters="abcdefghijklmnopqrstuvwxyz0123456789"
        new_string=""


        # iterate through string appending to new_string with lower case letters
        for char in s:
            if char.lower() in valid_characters:
                new_string=new_string+char.lower()

        # length of the new string is 0 or 1 and therefore a palindrome
        if len(new_string)==0 or len(new_string)==1:
            return True
        
        # create two pointers, one at each end of the new_string
        begin=0
        end=len(new_string)-1

        # iterate inwards until pointers cross
        while begin<end:
            # letters did not match
            if new_string[begin]!=new_string[end]:
                return False
            # advance pointers
            begin+=1
            end-=1
        # palindrome confirmed
        return True
        