# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 

n = int(input())
arr = list(map(int,input().split()))

def mean(a):
    s = sum(arr)
    return s/n

def std_dev(a,size,mu):
    dis = 0
    for i in a:
        dis+= (mu-i)**2
    return round(math.sqrt(dis/size),1)

mu = mean(arr)
print(std_dev(arr,n,mu))
