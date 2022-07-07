def solve(n):
    k=2
    sum=0
    while n>1:
        while n%k==0:
            sum+=k
            n/=k
        k+=1
    return sum

def factorSum(n):
    while n!=solve(n):
        n=solve(n);
    return n