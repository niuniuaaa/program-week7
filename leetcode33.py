# class Solution(object):
import pandas as pd
#import numpy as np
nums=[4,5,6,7,0,1,2]
def search(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    return binarySearch(nums, 0, len(nums) - 1, target)


# 新定义一个二分查找的函数
def binarySearch( nums, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2
    if nums[mid] == target:
        return mid

    if nums[mid] >= nums[left]:  # 左边是有序的
        if nums[left] <= target and target <= nums[mid]:  # 判断目标值在左半部分
            return binarySearch(nums, left, mid - 1, target)  # 递归，
        else:  # 否则，在右半部分
            return binarySearch(nums, mid + 1, right, target)
    else:  # 右边是有序的，同上述思想一致
        if nums[mid] <= target and target <= nums[right]:
            return binarySearch(nums, mid + 1, right, target)
        else:
            return binarySearch(nums, left, mid - 1, target)
num=search(nums, 0)
for i in range(0,len(nums)):
    print(nums[i])
print(num)
