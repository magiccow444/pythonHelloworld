# def binarySearch(nums, target):

    # Normal binary search

    # low = 0;
    # high = len(arr) - 1

    # while low <= high:
    #     middle = low + (high - low) // 2 
    #     value = arr[middle]

    #     print(value)

    #     if (value < target):
    #         low = middle + 1
    #     elif (value > target):
    #         high = middle - 1
    #     else:
    #         return middle

    # return -1


    # Binary search that will return the index of the target if it is found and if it is not found, it will return the index where the target should be inserted
    # It's a leet code problem btw

    # low = 0
    # high = len(nums) - 1

    # while (low <= high):
    #     middle = low + (high - low) // 2
    #     value = nums[middle]

    #     if (value < target):
    #         low = middle + 1
    #     elif (value > target):
    #         high = middle - 1
    #     else:
    #         return middle
    # if (value > target):
    #     return middle
    # else:
    #     return middle + 1