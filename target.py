#linear search program
def searchInset(lst, target):
    if not lst:  # Check if the list is empty
        return 0
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return len(lst)

lst = [[1, 2, 7, 8, 9, 10],9]
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
    
def find_target_in_nested_list(lst, target, path=None):
    if path is None:
        path = []  # Initialize the path for the first call

    for index, element in enumerate(lst):
        current_path = path + [index]  # Track the current index path
        if isinstance(element, list):  # If the element is a list, recurse into it
            find_target_in_nested_list(element, target, current_path)
        elif element == target:  # If the element is the target, print its path
            print(f"Target {target} found at index {current_path}")

# Example usage
lst = [[1, 2, 7, 8, 9, 10], 9,[3,6,9]]
target = 9

find_target_in_nested_list(lst, target)

    
    
