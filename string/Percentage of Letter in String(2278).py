class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        counter = 0

        for i in s:
            if i == letter:
                counter += 1
        return int(counter / len(s) * 100)