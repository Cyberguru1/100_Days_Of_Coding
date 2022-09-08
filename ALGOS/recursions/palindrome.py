
def is_palindrome(s:str) -> Any:
    n = len(s)
    if n <= 1:
        return True
    return (s[0] == s[n-1]) and is_palindrome(s[1:n-1])

is_palindrome("madam")