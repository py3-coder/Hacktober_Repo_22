def is_prime(m):  
    for i in range(2,m//2+1):  
        if(m%i==0):  
            return False
    return True
 
def n_primes(n):
    i = 1
    prime_list = []
    while True:
        i+=1
        if(is_prime(i)):
            prime_list+= [i]
            if len(prime_list)== n: break
    return prime_list
    
print(*n_primes(100))
