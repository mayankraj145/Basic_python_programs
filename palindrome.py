def is_palindrome(n):
    k=n[::-1]
    if k==n:
        return True
    return False
n=input("enter string")
print(is_palindrome(n))