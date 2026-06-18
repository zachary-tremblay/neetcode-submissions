class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        start = 0
        end = len(cleaned_text)-1
        print(cleaned_text)
        while (start <= end):
            if cleaned_text[start] != cleaned_text[end]:
                return False
            start += 1
            end -= 1
        return True
