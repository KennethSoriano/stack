'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
-Open brackets must be closed by the same type of brackets.
-Open brackets must be closed in the correct order.
-Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = {")": "(", "]":"[", "}":"{"}

        for c in s:
            # When using the "in" operator for a dictionary, it checks for the keys
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

'''
valid: 
Every Opening character has to have a closing character.
A closing character cannot start without an opening character.
True: (([[{}]]))
True because no closing character was introduced without its opening character. 
Every opening character has a closing character
False: (([)])
If a parenthesis is within another parenthesis, both the opening and closing characters must be 
within the parentheses
*Time STamp*

[]
Initially Input only opening characters
If a closing character is inputted, there must be a matching open character
Every opening character must have a closing


Add on as many opening characters.
If a closing character is being added, we must check if the most recent opening character is a match.

1.Use a stack
2.Use a dictionary with ending characters as keys
3.Use a foor loop to iterate through each char
    Check if the input char is an anding char in our dictionary
        .If so, check if the latest char added to our stack is a matching opening parenthesis.
            -If so, use the pop method to remove latest char from stack because the opening and closing parenthesis are match
            and we want to focus on the rest of the char.
            -If not, we return False because there's an invalid parenthesis due to the lack of opening char.
        .If not, we can append the opening char to our stack.

runtime:
O(n) because we iterate through the entire input string
space(n) because we organize the input strings

*TIMESTAMP*

'''