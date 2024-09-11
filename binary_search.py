def binary_search(lst,target):
    lst.sort()
    low=0
    mid=0
    high=len(lst)-1
    while low < high:
        mid= (low+high)//2
        if lst[mid]==target:
            return mid
        elif lst[mid]< target:
            low=mid+1
        else:
            high = mid-1
    return -1

lst=[4,7,2,9,1,8,3,6,5]
target=7
res=binary_search(lst,target)
if res != -1:
    print(f"Element {target} found at index {res} in the sorted list.")
else:
    print(f"Element {target} not found in the list.")