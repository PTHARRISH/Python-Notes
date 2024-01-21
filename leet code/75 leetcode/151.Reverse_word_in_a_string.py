def reverseWords(self, s: str) -> str:
    l=s.split()[::-1]
    return " ".join(l)