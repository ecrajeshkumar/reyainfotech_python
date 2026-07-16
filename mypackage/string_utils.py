
def reverse_string(s):
    """Return the reversed version of the input string."""
    return s[::-1]   # slicing trick

def count_vowels(s):
    """Count the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
