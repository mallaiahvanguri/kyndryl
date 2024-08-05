#linear search program
def searchInset(lst, target):
    if not lst:  # Check if the list is empty
        return 0
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return len(lst)

lst = [1, 2, 7, 8, 9, 10]
target =9
index = searchInset(lst, target)

#for index in lst:
if index < len(lst):
    print(f"The target element {target} is found at index {index}.")
else:
    print(f"The target element {target} is not found in the list.")
#Binary Search
def binarysearch(lst,target):
    low=0
    high=len(lst)
    while low<high:
        mid=(high+low)/2
        if lst[mid]==target:
            return mid
        if lst[mid]< target:
            low=mid+1
        if lst[mid]>target:
            high=mid
        return low
    
lst = [1, 2, 7, 8, 9, 10]
target =7
index = searchInset(lst, target)

#for index in lst:
if index < len(lst):
    print(f"The target element {target} is found at index {index}.")
else:
    print(f"The target element {target} is not found in the list.")
    
    
