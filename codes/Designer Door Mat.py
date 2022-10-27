nm = input().split()

n = int(nm[0])
m = int(nm[1])

for i in range(n//2):
    print((".|."*(2*i+1)).center(m, "-"))
    
print("WELCOME".center(m, "-"))

arr = []

for i in range(n//2):
    arr.append(str(".|."*(2*i+1)).center(m, "-"))
    
arr.reverse()

for i in arr:
    print(i)
