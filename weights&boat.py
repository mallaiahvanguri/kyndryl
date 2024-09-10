'''we are an array called people which contain weights of the people waiting to be 
ferried across a river. the ith person has the weight people[i]. Each boat can carry at the most two people at a time,
provided that the sum of the weights of those people does not exceed the given limit.
return the minimum nuber of the boats to be required to carry all the people'''
class Solution:
    def numreqboats(self,people,limit):
        people.sort() # arrange the weights in ascending order
        print(people)
        low=0 # set up a pointer at low end
        high=len(people) - 1
        n_boats=0
        while low <= high:
            n_boats+=1
            if people[low]+people[high]<= limit:
                low+=1
            high-=1
        return n_boats
        
people=[3,5,3,4,7]
limit=3
sol=Solution()
print(sol.numreqboats(people,limit))