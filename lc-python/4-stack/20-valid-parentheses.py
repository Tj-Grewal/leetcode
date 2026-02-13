class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        # key is to use a stack to keep track of things
        stack = []
        
        # dictionary of matching pairs
        parens = {"(":")","[":"]","{":"}"}

        for c in s:
            if c in parens: # Check if it's an opening bracket
                stack.append(c)
            else:
                # If stack is empty but we have a closing bracket -> False
                if not stack:
                    return False
                
                top = stack.pop()
                if parens[top] != c:
                    return False
                
        # Return True only if the stack is completely empty
        return len(stack) == 0

# Time: O(n) where n is the length of the string, since we need to check each character once.
# Space: O(n) in the worst case, if all characters are opening brackets, we would push all of them onto the stack.
