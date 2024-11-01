def fact(n):
    if (n==0 and n==1):
        return 1
    else:
        n*fact(n-1)
        return n
def main():       
 n=int(input('nter n'))
    
 fact(n)
