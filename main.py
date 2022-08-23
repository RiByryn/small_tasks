import sys
text = sys.stdin.read()

text = input()
sents = text.replace("!", ".").replace("?", ".").replace("-", "").replace(",", " ").replace(":", " ").replace(";", " ").split(".")
sents_without_spaces = []
count = 0
for i in range(len(sents)-1):
    sents_without_spaces.append(sents[i].strip())
for i in range(len(sents_without_spaces)):
    if sents_without_spaces[i][0].islower():
        count = count + 1
words = []
for sent_without_spaces in sents_without_spaces:
    words.extend(sent_without_spaces.split(" "))
for word in words:
    for j in range(1, len(word)):
        if word[j].isupper():
            count = count + 1
print(count)

