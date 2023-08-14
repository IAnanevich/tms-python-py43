# Дан произвольный список.
# Представьте его в обратном порядке. ([1, 2, 3] -> [3, 2, 1]

numbers_before = [1, 2, 3, 3, 4, 5]
numbers_after = numbers_before.copy()
numbers_after.reverse()

print("\nОсновной вариант .copy() и .reverse()")
print(f"Before: {numbers_before}")
print(f"After: {numbers_after}")

print("\nАльтернативный вариант [::-1]")
print(f"After alt.: {numbers_before[::-1]}")
