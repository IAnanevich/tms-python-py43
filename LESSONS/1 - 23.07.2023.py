
# 25.07.2023
# Theorem 3x + 1
# The 3x+1 problem, concerns the behavior of the iterates of the function which takes odd integers n to 3n+1 and even integers n to n/2.
# The 3x+1 conjecture asserts that, starting from any positive integer n, repeated iteration of this function eventually produces the value 1.

# Steps already passed
steps = 0

# Steps history
history = [float]

# Any positive integer to check
x = float(input("Enter X to check theorem '3x + 1' => "))
history.append(x)

# Let's check the input X
if x == 1:
    # Already 1
    s = x
    history.append(s)
else:
    # Run function 3x+1
    s = 3 * x + 1
    steps += 1
    history.append(s)

# Let's calc
while s != 1:
    # odd or even
    if (s / 2) != round(s / 2, 0):
        # odd integers 3x+1
        steps += 1
        s = 3 * s + 1
        history.append(s)
    else:
        # even integers x/2
        steps += 1
        s = s / 2
        history.append(s)

# print result
print(f"Steps to get infinite cycle is {steps}")

for y in history:
    print(y)
