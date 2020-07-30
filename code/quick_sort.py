def quick_sort(arr):

    n = len(arr)
    if n < 2: return arr

    pivot = arr[-1]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)
    # return quick_sort(left) + quick_sort(right)

print(quick_sort([1, 2,2,2,2,2,2,2,2,7,5,8,6,5,4,4,5,2,1,2,3]))
# a = list(reversed(range(2**24)))
# print(quick_sort(a))

class my_sort():

    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, start, end):
        if end <= start: return

        i, j = start + 1, end

        while i <= j:
            while i <= j and nums[i] <= nums[start]:
                i += 1
            while i <= j and nums[j] >= nums[start]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[start], nums[j] = nums[j], nums[start]
        self.quickSort(nums, start, j-1)
        self.quickSort(nums, j+1, end)