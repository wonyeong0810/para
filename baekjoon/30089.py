t = int(input())

for _ in range(t):
    s = input()
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            if i == 0:
                break
            s += s[i - 1::-1]
            break
    print(s)