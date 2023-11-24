
def ChkPrime(N):
    if N==1:
        return False
    for i in range(2,N):
        if(N % i ==0):
            return False
    else:
        return True

if __name__=="__main__":
    print(ChkPrime(5))
            

    