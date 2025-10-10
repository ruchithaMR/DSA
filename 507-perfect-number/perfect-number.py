from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        result=[1]
        for i in range(2,int(sqrt(num))+1):
            if num%i == 0:
                result.append(i)
                if i != num // i:
                    result.append(num // i)
        return sum(result)==num

    
        