# Hubert Jackowski
import numpy
import pathlib


class TextCompare:

    @staticmethod
    def hammingDistance(left: str, right: str) -> int:
        if len(left) != len(right):
            raise Exception("Different lengths")

        distance = 0
        for leftElement, rightElement in zip(left, right):
            if leftElement != rightElement:
                distance += 1

        return distance

    @staticmethod
    def hammingDistanceKeyboardSlip(left: str, right: str) -> int:
        def _neighboursOfKey(key) -> list[str]:
            rows = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
            rowsIndex, index = [(i, l.find(key)) for i, l in enumerate(rows) if key in l][0]
            rows = rows[rowsIndex - 1: rowsIndex + 2] if rowsIndex else rows[0: 2]
            return [
                row[index + i] for row in rows for i in [-1, 0, 1]
                if len(row) > index + i >= 0 and row[index + i] != key]

        if len(left) != len(right):
            raise Exception("Different Lengths")

        if (not left.isalpha()) or (not right.isalpha()):
            raise Exception("Symbol Not Supported, Enter Only Letters")

        distance = 0
        for leftElement, rightElement in zip(left, right):
            if leftElement in _neighboursOfKey(rightElement):
                distance += 1
            elif leftElement != rightElement:
                distance += 2

        return distance

    @staticmethod
    def getSimilar(word: str) -> list[str]:
        def _levenshteinDistance(a: str, b: str) -> int:
            if len(a) == 0:
                return len(b)
            if len(b) == 0:
                return len(a)
            if a[0] == b[0]:
                return _levenshteinDistance(a[1:], b[1:])
            return 1 + min([_levenshteinDistance(a[1:], b), _levenshteinDistance(a, b[1:]),
                            _levenshteinDistance(a[1:], b[1:])])

        dictionary = ("reel", "drugs", "disney", "handy", "competent", "retailer", "constraint", "illustrated", "old",
                      "bearing", "door", "got", "send", "surgery", "tracker", "green", "reading", "queensland",
                      "bahrain", "nato", "af", "ask", "restrictions", "breasts", "foster", "logic", "headline", "multi",
                      "yr", "lions", "albany", "modified", "hunt", "listen", "canadian", "turner", "seas", "candles",
                      "end", "determines", "seal", "deleted", "par", "rf", "depending", "recipes", "documentation",
                      "applied", "spanish", "declined", "tough", "hungary", "coordinate", "writers", "vpn", "companies",
                      "stuart", "valued", "philips", "toronto", "sc", "issued", "guest", "gamespot", "southern",
                      "farming", "suddenly", "muse", "long", "spiritual", "builder", "telling", "ottawa", "blind",
                      "worcester", "desktops", "bubble", "chronic", "redhead", "vsnet", "beside", "floor", "wendy",
                      "janet", "pew", "trigger", "payment", "crafts", "icq", "ws", "relating", "fairly", "contrary",
                      "cells", "wood", "low", "profit", "join", "kevin", "levels")
        distances = [_levenshteinDistance(word, dictionary[_]) for _ in range(len(dictionary))]
        dct = list(dictionary)

        if numpy.min(distances) == 0:
            return ["OK"]

        result = []
        for _ in range(3):
            bestIndex = numpy.argmin(distances)
            distances.pop(bestIndex)
            result.append(dct.pop(bestIndex))

        return result

    @staticmethod
    def getFileData(path: pathlib.Path):
        with open(path) as file:
            data = file.read()
            return data

    @staticmethod
    def getSymbolDensity(word: str) -> dict[str, float]:
        word = word.lower()
        symbolDensity = dict()
        alphaLength = 0
        for symbol in word:
            if symbol.isalpha():
                alphaLength += 1
                try:
                    symbolDensity[symbol] += 1
                except KeyError:
                    symbolDensity[symbol] = 1

        for key, value in symbolDensity.items():
            symbolDensity[key] = (value / alphaLength) * 100

        return symbolDensity

    @staticmethod
    def checkLanguageByLetter(wordSymbolDensity: dict[str, float]) -> str:
        letterLst = [
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z'
        ]
        englishLst = [
            8.167,
            1.492,
            2.782,
            4.253,
            12.702,
            2.228,
            2.015,
            6.094,
            6.966,
            0.253,
            1.772,
            4.025,
            2.406,
            6.749,
            7.507,
            1.929,
            0.095,
            5.987,
            6.327,
            9.056,
            2.758,
            0.978,
            2.360,
            0.250,
            1.974,
            0.074
        ]
        germanLst = [
            7.094,
            1.886,
            2.732,
            5.076,
            16.396,
            1.656,
            3.009,
            4.577,
            6.550,
            0.268,
            1.417,
            3.437,
            2.534,
            9.776,
            3.037,
            0.670,
            0.018,
            7.003,
            7.577,
            6.154,
            5.161,
            0.846,
            1.921,
            0.034,
            0.039,
            1.134
        ]
        polishLst = [
            9.986,
            1.482,
            4.436,
            3.293,
            9.052,
            0.312,
            1.377,
            1.072,
            8.286,
            2.343,
            3.411,
            3.882,
            2.911,
            5.785,
            8.413,
            3.101,
            0.003,
            4.571,
            4.946,
            3.966,
            2.347,
            0.034,
            4.549,
            0.019,
            3.857,
            6.566]
        englishDict = {letterLst[i]: englishLst[i] for i in range(len(letterLst))}
        germanDict = {letterLst[i]: germanLst[i] for i in range(len(letterLst))}
        polishDict = {letterLst[i]: polishLst[i] for i in range(len(letterLst))}

        languageGuessCount = {"english": 0, "german": 0, "polish": 0}
        keyLst = ["english", "german", "polish"]
        for key, value in wordSymbolDensity.items():
            valueLst = [abs(englishDict[key] - value), abs(germanDict[key] - value), abs(polishDict[key] - value)]
            languageGuessCount[keyLst[numpy.argmin(valueLst)]] += 1

        return max(languageGuessCount, key=languageGuessCount.get)

    @staticmethod
    def langTestLetter(path: pathlib.Path):
        return TextCompare.checkLanguageByLetter(TextCompare.getSymbolDensity(TextCompare.getFileData(path)))

    @staticmethod
    def getVowelDensity(word: str) -> dict[str, float]:
        word = word.lower()
        symbolDensity = dict()
        alphaLength = 0
        vowels = ["a", "e", "i", "o", "u", "y"]
        for symbol in word:
            if symbol.isalpha():
                alphaLength += 1
                destination = "vowel" if symbol in vowels else "consonant"
                try:
                    symbolDensity[destination] += 1
                except KeyError:
                    symbolDensity[destination] = 1

        for key, value in symbolDensity.items():
            symbolDensity[key] = (value / alphaLength) * 100

        return symbolDensity

    @staticmethod
    def checkLanguageByVowel(wordVowelDensity: dict[str, float]) -> str:
        englishDict = {"vowel": 40.33, "consonant": 59.67}
        germanDict = {"vowel": 38.55, "consonant": 61.46}
        polishDict = {"vowel": 44.28, "consonant": 55.72}

        languageGuessCount = {"english": 0, "german": 0, "polish": 0}
        keyLst = ["english", "german", "polish"]
        for key, value in wordVowelDensity.items():
            valueLst = [abs(englishDict[key] - value), abs(germanDict[key] - value), abs(polishDict[key] - value)]
            languageGuessCount[keyLst[numpy.argmin(valueLst)]] += 1

        print(wordVowelDensity)
        return max(languageGuessCount, key=languageGuessCount.get)

    @staticmethod
    def langTestVowel(path: pathlib.Path):
        return TextCompare.checkLanguageByVowel(TextCompare.getVowelDensity(TextCompare.getFileData(path)))

    @staticmethod
    def longestCommonSubstring(left: str, right: str) -> str:
        result = ""
        len1, len2 = len(left), len(right)
        for i in range(len1):
            match = ""
            for j in range(len2):
                if i + j < len1 and left[i + j] == right[j]:
                    match += right[j]
                else:
                    if len(match) > len(result):
                        result = match
                    match = ""

        return result

    @staticmethod
    def longestCommonSubsequence(left: str, right: str) -> str:
        m = len(left)
        n = len(right)
        L = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif left[i - 1] == right[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        lcs = ""
        i = m
        j = n
        while i > 0 and j > 0:
            if left[i - 1] == right[j - 1]:
                lcs += left[i - 1]
                i -= 1
                j -= 1
            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return lcs[::-1]

    @staticmethod
    def levenshteinDistance(a: str, b: str) -> int:
        if len(a) == 0:
            return len(b)
        if len(b) == 0:
            return len(a)
        if a[0] == b[0]:
            return TextCompare.levenshteinDistance(a[1:], b[1:])
        return 1 + min([TextCompare.levenshteinDistance(a[1:], b), TextCompare.levenshteinDistance(a, b[1:]),
                        TextCompare.levenshteinDistance(a[1:], b[1:])])
