g1=100
def is_palindrome(s):
    if type(s) == int:
        s=str(s)
    print(g1,g2)
    return s == s[::-1]

def ispalindrome(s=121):
    if type(s) == int:
        s=str(s)
    global g2
    g2=200
    print(g2)
    return s == s[::-1]
