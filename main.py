import sys
import re

# text = sys.stdin.read()
text = "This sentence iz correkt! -It Has,No mista;.Kes et oll.\nBut there are two BIG mistakes in this one!\nand here is one more."
# text = "This is a message with thREE mistakes::: and four sentences!!! Hope i;:;:t helps"
# text = "Usual sentence."
# text = ";a!b!c!d!"
sents = re.split("[!?.]", text)

count = 0

for sent in sents:
    comp = re.compile("[A-Za-z]+")
    words = []
    if len(sent) > 0 and comp.findall(sent)[0].islower():
        count = count + 1
    words.extend(comp.findall(sent))
    for word in words:
        for j in range(1, len(word)):
            if word[j].isupper():
                count = count + 1
print(count)




