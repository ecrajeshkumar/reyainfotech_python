# palindrome words
# s = "racecar"
s = "hello"
s = "A man, a plan, a canal: Panama"
# cleaned_s = ''.join(c.lower() for c in s if c.isalnum())  ## Remove non-alphanumeric and convert to lowercase
is_palindrome = s == s[::-1]
print(f"'{s}' is a palindrome ?: {is_palindrome}")
