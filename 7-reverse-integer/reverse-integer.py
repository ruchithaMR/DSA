class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x=str(abs(x))
        result=0
        result=int(x[::-1])
        if result<-2**31 or result>2**31-1:
            return 0
        return sign *result
        
    