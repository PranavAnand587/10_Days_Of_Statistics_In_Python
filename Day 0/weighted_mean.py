n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

def weighted_mean(num,wts,size):
    wsum,s = 0,sum(wts)
    for i in range(size):
        wsum += num[i]*wts[i]
    return round(wsum/s,1)

print(weighted_mean(x,w,n))
