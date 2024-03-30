n = int(input())

pileup = 1  
count = 1
while n > pileup :
    pileup += 6 * count  
    count += 1  
print(count)