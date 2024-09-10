'''write a function that return True if a positive interger supplied to it is the sqrt
of some integer otherwise return false. However, you are not allowed to use any library
function like SQRT'''
class Solution:
    def isperfectsqrt(self,num:int) ->bool:
        for i in range(1,num+1):
            if num==i*i:
                return True
        return False
'''summation of arithmetic progression{sum of n odd numbers is n2}'''    
class Solution:
    def isperfectsqrt(self, n:int) ->bool:
        sum=0
        i=1
        while sum < n:
            sum+=i
            if sum==n:
                return True
            i+=2
        return False
sol=Solution()
for i in range(1,10):
    print(i,sol.isperfectsqrt(i))