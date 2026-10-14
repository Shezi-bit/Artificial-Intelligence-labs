
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high)//2

        if arr[mid] == target:
            return mid          # found, return index
        elif arr[mid] < target:
            low = mid + 1  
        else:           # search right half
            high = mid - 1      # search left half
        
    return -1


data = [2, 5, 8, 12, 16, 23, 38]
print(binary_search(data, 23))  # 5
print(binary_search(data, 7))   # -1