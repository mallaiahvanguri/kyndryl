'''write a function that return True if a positive interger supplied to it is the sqrt
of some integer otherwise return false. However, you are not allowed to use any library
function like SQRT'''
class Solution:
    def isperfectsqrt(self,num:int) ->bool:
        for i in range(1,num+1):
            if num==i*i:
                print(i,i,num)
                return True
        return False
sol=Solution()
for i in range(1,10):
    print(i,sol.isperfectsqrt(i))