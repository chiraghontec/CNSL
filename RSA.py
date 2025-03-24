from math import gcd

def RSA(p:int, q:int, message:int):
    n = p*q
    t = (p-1)*(q-1)

    for e in range(2,t):
        if gcd(e,t) == 1:
            break
    d = pow(e,-1,t)

    ct = pow(message,e,n)
    print(f"Encrypted message is {ct}")
    mes = pow(ct,d,n)
    print(f"Decrypted message is {mes}")

RSA(p=3,q=7,message=9)
RSA(p=3,q=7,message=7)