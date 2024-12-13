class Solution:
    def countBits(self, n: int) -> List[int]:
        countarray = []
        for i in range(n + 1):
            count = 0
            num = i
            while num > 0:
                count += num % 2  
                num = num // 2 
            countarray.append(count)  # Correctly append count to countarray
        return countarray  # Return countarray after the loop completes