def binary_search(nums, target):
    lo, hi = 0,  len(nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2

        # print('lo', lo)
        # print('mid', mid)
        # print('hi', hi)

        # If you found the number
        if target == nums[mid]:
            return mid

        elif nums[mid] > target:
            hi = mid - 1

        elif nums[mid] < target:
            lo = mid + 1
         
    return -1

def binary_search_max(nums, target):
    lo, hi, res = 0, len(nums) - 1, -1
    
    while lo <= hi:
        mid = (lo + hi) // 2

        # If you found the number
        if nums[mid] == target:
            res = mid
            lo = mid + 1

        elif nums[mid] < target:
            lo = mid + 1

        elif target < nums[mid]:
            hi = mid - 1
         
    return res

nums = [5,7,7,8,8,10] 
target = 8

print(binary_search(nums, target), binary_search_max(nums, target))
