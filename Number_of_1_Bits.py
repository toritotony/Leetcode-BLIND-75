class Solution:
    def hammingWeight(self, n: int) -> int:
        q = n
        r = 0
        b = []
        while q > 0:
            r = q % 2
            b.append(r)  # Use append to add elements to the list
            q = q // 2
        
        # Move the count calculation and return statement outside the loop
        count = sum(1 for i in b if i == 1)
        return count
 
######################################################################################################

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            r = n % 2   # Get the last bit
            if r == 1:
                count += 1  # Increment count if the last bit is 1
            n = n // 2   # Remove the last bit
        return count
