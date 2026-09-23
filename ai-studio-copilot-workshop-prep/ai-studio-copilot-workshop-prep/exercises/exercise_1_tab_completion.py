"""
Exercise 1: Tab completion warm-up

None of the functions below do anything yet. Each one has a comment
describing what it should do and a `pass` placeholder instead of real
code.

For each function: delete the `pass` line, put your cursor there, and
start typing. Once GitHub Copilot is enabled, it will offer a suggestion as gray "ghost
text." Press Tab to accept it, Esc to dismiss it, or keep typing your
own version.
"""

# Notice that when we delete the pass the file still suggest 'pass' as the correct value. 
# Can anyone tell me why?
# Looking for 'because the provided context around where the cursor is pointing to 'pass' being the wanted value'

def square(n):
    # Return the square of n.
    
    # delete pass and type return
    # why does it now suggest the correct n*n?
    # Looking for 'because the context around the cursor changed'
    pass

def is_prime(n):
    # Return True if n is prime, False otherwise.
    
    # One more time for the peeps in the back
    pass

# When using GitHub copilot it provides context to the LLM in this order:
# - Code around the cursor; prefix and suffix; names; signature and types; imports; comments/docstrings; nearby examples; syntax and indentation.
# - Relevant open files, selected workspace snippets, recent edit history, language-service information, and diagnostics for some next-edit fixes.
# - Considerations: Model choice, token budget, account/organization policy, extension version.
# - Not safe to assume: The whole repository, every open tab, your terminal output, the current Chat conversation, or any particular file will be included in every completion.

# Using learnings above
# Why do we no get good suggestions for this function
# Looking for 'it's vague and there really isn't any codex to be gain'
def process(items):
    pass

# Improve by adding the correct context
# Import libraries
from collections.abc import Iterable

# Update the name
def normalize_email_rows(
    rows: Iterable[dict[str, str]], # Provide typing input and return
) -> list[dict[str, str]]: # [{"email": "mail@email.com"}, ...]
    # Good clean doc string
    """Return new rows with trimmed, lowercase email addresses.

    Skip rows without an email, preserve order, and do not mutate input.
    """

# Add a little TDD into the mix, make sure to open it to the side window and you can even highlight it
from context_lab import normalize_email_rows

def test_normalize_email_rows():
    rows = [{"email": "  ADA@EXAMPLE.COM  "}, {"name": "Grace"}]
    assert normalize_email_rows(rows) == [{"email": "ada@example.com"}]
    
# Name: use domain-specific symbols instead of data, process, or handle.
# Shape: add types, parameters, returns, imports, and data structures.
# Contract: state constraints and edge cases in a compact docstring or comment.
# Example: put a representative call or test nearby.
# Neighborhood: open the few files that define the behavior or demonstrate the repository pattern.

# Answer key
# def square(n):
#     return n * n

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def filter_by_length(strings, min_length):
#     return [s for s in strings if len(s) >= min_length]

