collection = ['a', 'e', 'i', 'o', 'u']

while True:
    count = 0
    sentence = input().lower()

    if sentence == '#':
        break
    for s in sentence:
        if s in collection:
            count += 1
    print(count)