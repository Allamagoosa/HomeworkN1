#!/usr/bin/python
def eratos(n):
    """Test========================
    >>> for i in eratos(3): print(i)
    2
    3
    """

    emas = range(2, n+1)
    #print "initial emas:\n",emas
    p = 2
    
    while p*p <= n:
        i0=emas.index(p*p)
        for i in range(i0, n-1, p):
            emas[i]=0
    
        for j in range(1, n-1):
            if emas[j] != 0 and emas[j] > p:
	        p = emas[j]	      
	        break
	        
    for item in emas:
        if item != 0: yield item

print "\nAncient knowledge: "        
for i in eratos(30):
    print(i)

if __name__ == "__main__":
    import doctest
    doctest.testmod()