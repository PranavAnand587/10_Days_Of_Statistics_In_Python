size = int(input())
arr = list(map(int, input().split()))

def mean(a):
    l = len(a)
    s = sum(a)
    return s/l

def median(a):
    a.sort()
    mid = 0
    if size%2==0:
        mid = (a[size//2] + a[size//2 - 1]) / 2
    else:
        mid = a[(size - 1)//2]
    return mid

def mode(a):
    current,maxi,count,mode = 0,0,0,0
    for i in a:
        if (i == current):
            count += 1
        else:
            count = 1
            current = i
        if (count > maxi):
            maxi = count
            mode = i
    return mode

print(mean(arr))
print(median(arr))
print(mode(arr))

