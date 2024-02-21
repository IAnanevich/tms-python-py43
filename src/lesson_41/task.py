def solve(nums: list, targ: int) -> bool:
    seen_numbers = set()

    for num in nums:
        diff = targ - num
        if diff in seen_numbers:
            return True
        seen_numbers.add(num)
    return False


numbers = [2, 3, 5, 11, 1, 100, 5, 4, -4, 23, 15, 17, 1]
target = 1000
print(solve(numbers, target))
