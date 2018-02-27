class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}

        for i in range(len(nums)):
            #print(i)
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                print(buff_dict)
                buff_dict[target - nums[i]] = i


if __name__ == '__main__':
    num = [1, 4, 3, 5, 6, 8, 100, 90]
    b_target = 101
    solution = Solution()
    print(solution.twoSum(num, b_target))

