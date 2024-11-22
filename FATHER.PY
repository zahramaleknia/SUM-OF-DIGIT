def sum(n):
    return sum(int(digit)for digit in str(n))
def first_number(num):
    if num%i==0:
        return False
    for i in range(2,int(num**0.5)+1):
        if num %i==0:
            return False
    return True
def digit(n):
    t=0
    for i in range(2,n+1):
        if n%i==0 and first_number(i):
            t+=1
    return t