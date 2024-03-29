# Hubert Jackowski
from TextCompare import TextCompare

print("-" * 20, "Longest Common Substring", "-" * 20)
print(TextCompare.longestCommonSubstring("test1t", "test2t"))
print(TextCompare.longestCommonSubstring("konwalia", "zawalina"))

print("-" * 20, "Longest Common Substring With Spacing", "-" * 20)
print(TextCompare.longestCommonSubsequence("ApqBCrDsEF", "tABuCvDEwxFyz"))
print(TextCompare.longestCommonSubsequence("TEST", "TESThgdfd"))
print(TextCompare.longestCommonSubsequence("TESTgdsefgT", "TESTpT"))

print("-" * 20, "Levenshtein Distance", "-" * 20)
print(TextCompare.levenshteinDistance("test1", "test1234"))
print(TextCompare.levenshteinDistance("test1", "test1"))
print(TextCompare.levenshteinDistance("test1", "test"))
