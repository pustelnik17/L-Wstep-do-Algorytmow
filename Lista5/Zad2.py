# Hubert Jackowski
from TextCompare import TextCompare
import pathlib

print("-" * 20, "Letter Frequency", "-" * 20)
print(TextCompare.getSymbolDensity("Test1"))
print(TextCompare.getSymbolDensity("Test"))
print(TextCompare.getSymbolDensity("Testy"))

print("-" * 20, "Language Detection By Letter", "-" * 20)
print(TextCompare.langTestLetter(pathlib.Path.cwd() / "EnglishLangTest.txt"))
print(TextCompare.langTestLetter(pathlib.Path.cwd() / "GermanLangTest.txt"))
print(TextCompare.langTestLetter(pathlib.Path.cwd() / "PolishLangTest.txt"))

print("-" * 20, "Language Detection By Vowel", "-" * 20)
print(TextCompare.langTestVowel(pathlib.Path.cwd() / "EnglishLangTest.txt"))
print(TextCompare.langTestVowel(pathlib.Path.cwd() / "GermanLangTest.txt"))
print(TextCompare.langTestVowel(pathlib.Path.cwd() / "PolishLangTest.txt"))
