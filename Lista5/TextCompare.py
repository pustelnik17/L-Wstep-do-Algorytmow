# Hubert Jackowski
import numpy


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
    def dictionarySimilar(word: str) -> list[str]:
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
            return [dct[numpy.argmin(distances)]]

        result = []
        for _ in range(3):
            bestIndex = numpy.argmin(distances)
            distances.pop(bestIndex)
            result.append(dct.pop(bestIndex))

        return result
