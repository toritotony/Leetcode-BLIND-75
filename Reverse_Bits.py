class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, '032b')
        count = 0
        array = [int(x) for x in str(n)]
        array = array[::-1]
        for i in range(len(array)):
            count += 0 if array[i] == 0 else pow(2, (len(array)-1-i))
            print(count)
        return count
    
#######################################################################

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1  
            result |= (n & 1)  
            n >>= 1  
        return result