class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If there are still remaining k to remove, pop the last k digits from the stack
        while k > 0:
            stack.pop()
            k -= 1
        
        # Convert the stack to a string (with leading zeros removed) and return it
        return "".join(stack).lstrip("0") or "0"