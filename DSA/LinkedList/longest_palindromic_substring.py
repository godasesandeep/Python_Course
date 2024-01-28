# Longest Polindromic substring

    
s='forgeeksskeegforakabakaakabak'
n=len(s)
maxlen=0

for c in range(n):
    start,end=c,c #Expand from center for odd palindromic string
    while( start>=0 and end<n and s[start]==s[end]):
        if maxlen<(end-start+1):
            maxlen=end-start+1
            ls1=s[start:end+1]
        start -=1
        end +=1

for c in range(n):
    start,end=c,c+1 #Expand from center for even palindromic
    while(start>=0 and end<n and s[start]==s[end]):
        if maxlen<(end-start+1):
            maxlen=end-start+1
            ls2=s[start:end+1]
        start -=1
        end +=1

print(ls1 if len(ls1) > len(ls2) else ls2)

        

# Longest Polindromic substring -2nd method

#s='forgeeksaskeegfor'
#s='tpopk'
n=len(s)
maxlen=0
for i in range(2,n):
    for j in  range(n-i+1):
        f=s[j:i+j]
        r=f[::-1]
        if f==r:
            if maxlen<len(f):
                maxlen=len(f)
                string=f
                           
print(string)