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
            # print(i)
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                # print(buff_dict)
                buff_dict[target - nums[i]] = i


if __name__ == '__main__':
    num = [1, 4, 3, 5, 6, 8, 100, 90]
    b_target = 101
    solution = Solution()
    print(solution.twoSum(num, b_target))

'''

给定一个整型列表，找出能相加起来等于一个特定目标数字的两个数
本题的解决方案是采用字典
字典有键和值两个属性
1. 首先定义一个空的字典，然后通过程序慢慢填充字典；
2. 首先从下标为x(x从0开始)的值[x]判断是否存在字典的键中，若不存在就拿特定目标数减去这个值[x]作为字典的键，下标x做这个键对应的值
3. 依次判断列表的值是否在字典的键中
4. 若列表的值在创建的字典中存在了，则返回本次键对应的值和x

'''