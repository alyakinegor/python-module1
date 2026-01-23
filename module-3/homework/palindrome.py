def is_palindrome(s):
    rev = list(s)
    rev.reverse()
    rev = ''.join(rev)
    if s == rev:
        print(True)
    else:
        print(False)
is_palindrome('доход')
