import sys
import re

text = sys.stdin.read()
# text = "This sentence iz correkt! -It Has,No mista;.Kes et oll.\nBut there are two BIG mistakes in this one!\nand here is one more."
# text = "This is a message with thREE mistakes::: and four sentences!!! Hope i;:;:t helps"
# text = "Usual sentence."
# text = ";a!b!c!d!"
sents = re.split("[!?.]", text)

count = 0
# print(sents)
for sent in sents:
    comp = re.compile("[A-Za-z]+")
    words = []
    words = comp.findall(sent)
    if len(words) > 0:
        if words[0][0].islower():
            count = count + 1
        # print(words)
        for word in words:
            for j in range(1, len(word)):
                if word[j].isupper():
                    count = count + 1
print(count)




