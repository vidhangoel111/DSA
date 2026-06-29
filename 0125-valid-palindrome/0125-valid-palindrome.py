class Solution(object):
    def isPalindrome(self, s):
        n = len(s)
        p1 = 0
        p2 = n-1
        while p1<p2:
            if not s[p1].isalnum():
                p1+=1
            elif not s[p2].isalnum():
                p2-=1
            else:
                if s[p1].lower()!=s[p2].lower():
                    return False
                p1+=1
                p2-=1
        return True

