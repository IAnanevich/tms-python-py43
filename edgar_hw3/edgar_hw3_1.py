# Enter  2 words. First method f-string . comment
two_words = input("Enter 2 words: ")

# add to list
words = two_words.split()

# revers
reversed_words = words[1] + " " + words[0]

final_result = f"!{reversed_words}!"

print("First method:", final_result)

# -------------------------------------------------------------------------------------
# Enter 2 words. Second method use format()

two_words_two = input("Enter 2 words: ")

# add to list

words_two = two_words_two.split()

# reverse
reverse_words_two = words_two[1] + " " + words_two[0]

# add !
final_result_two = "!{} {}!".format(*reverse_words_two.split())

# print

print("Second method ", final_result_two)

# ---------------------------------------------------------------------------------------
