# ID: 20
# URL: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#               An input string is valid if:              
#                 -Open brackets must be closed by the same type of brackets.
#                 -Open brackets must be closed in the correct order.


class Solution:
    def isValid(self, s: str) -> bool:
   
        """
        example= "[({})]"
        algorithm:
        - check if the initial length of input is 1
        - push first char to stack ["["]
        - if next char is a matching closing bracket, remove the previous char from array
        - else add it to the array 
        - after iterating through the string, if the length of the array not None then return false
        - else return True
        """
    
        closing_paren={ "}":"{",
                       "]":"[",
                       ")":"("     
        }
        
        
        # input string length is one and has no matching parenthesis
        if len(s)==1:
           return False
        # first in first out stack data structure
        stack=[]
        # iterate through the string adding the open parentheses and popping if a matching closing parenthesis is found
        for paren in s:
            try:
                # push the opening parenthesis to top of stack
                if paren in closing_paren.values():
                    stack.append(paren)
                # pop the top of the stack if it matches a closing parenthesis
                elif closing_paren[paren]==stack[-1]:
                    stack.pop()
                # stack imabalance, not a valid input
                else:
                    return False
            # accounts for the case '}{' since stack[-1] will raise an exception 
            except IndexError:
                return False
            
        # imbalanced stack
        if len(stack)>0:
            return False
        
        # parentheses all matched, valid input
        return True