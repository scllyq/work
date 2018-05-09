def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while True:
            dic = []
            n = 0

            if n >= len(nums):
                return nums
                break
            if nums[n] in dic:
                nums.pop(n)
                n -= 1
            else:
                dic.append(nums[n])
                n += 1
a=[1,1,2,2]
print(removeDuplicates(a))
