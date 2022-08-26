import sys
import re

text = sys.stdin.read()
# text = "This sentence iz correkt! -It Has,No mista;.Kes et oll.\nBut there are two BIG mistakes in this one!\nand here is one more."
# text = "This is a message with thREE mistakes::: and four sentences!!! Hope i;:;:t helps"
# text = "Usual sentence."
sents = re.split("[!?.]", text)
# print(sents)
sents_without_spaces = []
count = 0
for sent in sents:
    sents_without_spaces.append(sent.strip())
# print(sents_without_spaces)
for i, sent_without_spaces in enumerate(sents_without_spaces):
    if len(sent_without_spaces) > 1 and sent_without_spaces[0].islower():
        count = count + 1
words = []
for sent_without_spaces in sents_without_spaces:
    comp = re.compile("[A-Za-z]+")
    words.extend(comp.findall(sent_without_spaces))
# print(words)
for word in words:
    for j in range(1, len(word)):
        if word[j].isupper():
            count = count + 1
print(count)




