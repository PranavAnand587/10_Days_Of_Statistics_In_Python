# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

def median(a):
    length = len(a)
    if(length%2==0):
        return (a[length//2] + a[length//2 - 1])/2
    else:
        return a[(length-1)//2]

q_two = median(arr)
q_one,q_three =0,0

if(n%2!=0):
    q_one = median(arr[:n//2])
    q_three = median(arr[n//2 + 1:])
else:
    q_one = median(arr[:n//2])
    q_three = median(arr[n//2:])

print(int(q_one))
print(int(q_two))
print(int(q_three))

