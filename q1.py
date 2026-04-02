def is_palindrome(string):
    left=0
    right=len(string)-1
    while left<right:
        if string[left]!=string[right]:
            return False
        left+=1
        right-=1
    return True
def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    longest=""
    i=0
    while i<len(s):
        j=i+2
        while j<=len(s):
            string=s[i:j]
            if is_palindrome(string):
                if len(string)>len(longest):
                    longest =string
            j+=1
        i+=1
    return longest