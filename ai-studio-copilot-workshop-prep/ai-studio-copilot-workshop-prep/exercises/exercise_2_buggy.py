"""
Exercise 2: Explain and fix a bug with Copilot Chat

The function below is real, runnable code. It computes the average of
a list of numbers, but it has a bug.

1. Select the `average` function, including the def line.
2. Open Copilot Chat and ask it to explain what the function does.
3. Run this file. Watch the second call crash.
4. Ask Copilot Chat why the crash happens, then ask it to fix the
   function. Read the fix before you accept it. Does it handle an
   empty list the way you would want it to?
"""

# Prompt: Fix this?
# How to improve this prompt?
# Looking for:
# - Adding the error message
# - Adding how it was ran
# - Adding what has already been tried to fix it

# Use the chat as a rubbing duck session

# When bug fixing we can improve our suggestions by:
# - Use TDD, if there is an expected value write a unit test and have it open next to the buggy code
# - Improve your prompt, don't just say fix this. You should provide how you ran the function and the output at the very least.
# - Matt Pocock has some great skills to look at

# Answer key
def average(numbers):
    if not numbers:
        return 0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


print(average([1, 2, 3, 4, 5]))
print(average([]))

# def average(numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total / len(numbers)


# print(average([1, 2, 3, 4, 5]))
# print(average([]))  # This line raises ZeroDivisionError.