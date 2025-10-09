class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums=x
        result=0
        while nums>0:
            ld=nums%10
            result=(result*10)+ld
            nums=nums//10
        return x==result
        