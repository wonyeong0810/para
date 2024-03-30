li = [1,2,3]

n = int(input(""))

for i in range(n):
    x,y = map(int, input("").split())
    
    xi = li.index(x)
    yi = li.index(y)
    
    li[xi], li[yi] = li[yi], li[xi]

print(li[0])
