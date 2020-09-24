"""
Question : EASY
[389. Find the Difference](https://leetcode.com/problems/find-the-difference/)
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:
Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor, n, i = 0, len(s), 0

        while i < n:
            xor ^= ord(s[i])
            xor ^= ord(t[i])
            i += 1

        xor ^= ord(t[-1])

        return chr(xor)


# Runtime: 28 ms, faster than 92.15% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 75.86% of Python3 online submissions
