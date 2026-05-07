class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)

        start = 0
        end = length - 1
        while (start <= end):

            if not self.is_valid(s[start]):
                start += 1
                continue

            if not self.is_valid(s[end]):
                end -= 1
                continue

            print(s[start].lower() , s[end].lower())

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True
    
    def is_valid(self, char):
        return (ord('a') <= ord(char) <= ord('z') or
               ord('A') <= ord(char) <= ord('Z') or 
               ord('0') <= ord(char) <= ord('9'))

        