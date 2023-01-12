import time
tic = time.perf_counter()
#recurusion
def recurusion_fib(n):
   if n <= 1:
       return n
   else:
       return(recurusion_fib(n-1) + recurusion_fib(n-2))

print(recurusion_fib(38))
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")

tic = time.perf_counter()
#Dynamic programming using Memoized method
def fib(n,lst):
   
    if n <= 1:
        return n
  
    if lst[n] != -1:
        return lst[n]
    
    lst[n] = fib(n-1,lst) + fib(n-2,lst)
    return lst[n]
    

lst = [-1 for i in range(39)]    
print(fib(38,lst))
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")


#Dynamic programming using Tabular method
tic = time.perf_counter()
def fib(n):
   
    if n <= 1:
        return n
    F = [-1 for i in range(n+1)]
    F[0] = 0
    F[1] = 1
    for i in range(2,n+1):
        F[i] = F[i-2] + F[i-1]
    return F[n]
    

print(fib(38))
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")