def part_one(nums):
    for i in nums:
        for j in nums:
            if i + j == 2020:
                return i * j


def part_two(nums):
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 2020:
                    return i * j * k


with open('01-data.txt') as f:
    inputs = [
        int(line)
        for line in f
    ]
    print(part_one(inputs))
    print(part_two(inputs))