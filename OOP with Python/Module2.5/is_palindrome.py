def is_palindrome(s):
     return s == s[::-1]


s=input()
ans = is_palindrome(s)

if ans:
    print("YES")
else:
    print("NO")