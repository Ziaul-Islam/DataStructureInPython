counter = 0
memo = [None] * 5

def fib(n):
    global counter
    counter += 1
    print("Call n : ",n)
    print(counter," : ",memo)
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

#print(memo)
print("fib : ",fib(3))
print(memo)
print("function call : ",counter)

