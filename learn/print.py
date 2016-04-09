#test yield
def acall(n):
    while n > 0:
        yield n
        n-=1  
"""
    for i in range(n):
        yield i+1
"""        
    
for n in acall(5):
    print (n)

