# Hubert Jackowski
from TextCompare import TextCompare

print("-"*20, "Hamming Distance", "-"*20)
left, right = "karolin", "kathrin"
print(left, right, TextCompare.hammingDistance(left, right))
left, right = "karolin", "kerstin"
print(left, right, TextCompare.hammingDistance(left, right))
left, right = "kathrin", "kerstin"
print(left, right, TextCompare.hammingDistance(left, right))
left, right = "0000", "1111"
print(left, right, TextCompare.hammingDistance(left, right))
left, right = "2173896", "2233796"
print(left, right, TextCompare.hammingDistance(left, right))

print("-"*20, "Hamming Distance Keyboard Slip", "-"*20)
left, right = "kathrin", "kerstin"
print(left, right, TextCompare.hammingDistanceKeyboardSlip(left, right))
left, right = "wer", "wee"
print(left, right, TextCompare.hammingDistanceKeyboardSlip(left, right))
left, right = "wer", "wer"
print(left, right, TextCompare.hammingDistanceKeyboardSlip(left, right))
left, right = "wer", "wey"
print(left, right, TextCompare.hammingDistanceKeyboardSlip(left, right))


print("-"*20, "Dictionary Check", "-"*20)
print(TextCompare.getSimilar("reel"))
print(TextCompare.getSimilar("reels"))
print(TextCompare.getSimilar("ree"))
print(TextCompare.getSimilar("rf"))
