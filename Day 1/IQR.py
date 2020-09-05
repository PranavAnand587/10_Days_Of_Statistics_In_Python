# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))
s = []

for i in range(n):
    s += [x[i]] * f[i]

s.sort()
size = len(s)
def median(a):
    mid = 0
    size = len(a)
    if size%2==0:
        mid = (a[size//2] + a[size//2 - 1]) / 2
    else:
        mid = a[size//2]
    return mid

if(n%2==0):
    q_one = median(s[:size//2])
    q_three = median(s[size//2:])
else:
    q_one = median(s[:size//2])
    q_three = median(s[(size//2 + 1):])

print(round(float(q_three-q_one),1))

