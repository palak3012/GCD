
def gcd(a,b):
    if(b==0):
        return a
    else:
        c=gcd(b,a%b)
        return(c)
print('gcd of two numbers')
ans=gcd(70,17.5)
print(ans)
