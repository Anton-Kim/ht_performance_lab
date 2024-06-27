from sys import argv

numbers_path = argv[1]

with open(numbers_path, encoding='utf-8') as numbers:
    nums = [int(line.strip()) for line in numbers.readlines()]


def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)


print(min_moves_to_equal_elements(nums))
