import sys
import string
import os

fname = input("Enter the file name: ")

if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

infile = open(fname, "r")

file_contents = ""

for line in infile:
    for ch in line:
        if ch not in string.punctuation:
            file_contents = file_contents + ch
        else:
            file_contents = file_contents + " "

wordFreq = {}
wordList = file_contents.lower().split()

for word in wordList:
    if word not in wordFreq:
        wordFreq[word] = 1
    else:
        wordFreq[word] += 1

sortedWordFreq = sorted(wordFreq.items(), key=lambda x: x[1], reverse=True)

print("=" * 50)
print("10 most frequently occurring words with their counts")
print("=" * 50)

for i in range(min(10, len(sortedWordFreq))):
    print(sortedWordFreq[i][0], ":", sortedWordFreq[i][1], "times")

infile.close()