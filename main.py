# text = input()
text = "This sentence iz correkt! -It Has,No mista;.Kes et oll.\nBut there are two BIG mistakes in this one!\nand here is one more."
sents = text.replace("!", ".").replace("?", ".").replace("-", "").replace(",", " ").replace(":", " ").replace(";", " ").split(".")
sents_without_spaces = []
count = 0
for i in range(len(sents)-1):
    sents_without_spaces.append(sents[i].strip())
for i in range(len(sents_without_spaces)):
    if sents_without_spaces[i][0].islower():
        count = count + 1
print(text)
print(count)
worlds = []
for i in range(len(sents_without_spaces)):
    worlds.extend(sents_without_spaces[i].split(" "))
for i in range(len(worlds)):
    for j in range(1, len(worlds[i])):
        if worlds[i][j].isupper():
            count = count + 1
print(sents_without_spaces)
print(worlds)
print(count)

