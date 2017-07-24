mod = 1000000007
def fib(n):
    a=2
    b=3
    c=a+b
    if n==0:
        return 0
    elif n==1:
        return a
    elif n==2:
        return b
    else:
        for i in range(3,n+1,1):
            c = a+b
            a=b
            b=c
        return c
    


test_case = long(raw_input())
for i in range(test_case):
    n = long(raw_input())
    result=fib(n)
    print result%mod
    
