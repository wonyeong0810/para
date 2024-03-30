word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 1

for i in range(len(word)-1):
    if alphabet.index(word[i]) < alphabet.index(word[i+1]):
        continue
    else:
        count += 1

print(count)