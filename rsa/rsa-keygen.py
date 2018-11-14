#Students: Hayden Coffey, Aaron Johnson
#Course: COSC 483
#Project 2

import halib2_Electric_Boogaloo
import math
from Crypto.Util import number

if __name__ == "__main__":
    #Read in cmd line arguments
    args = halib2_Electric_Boogaloo.arg_return(1)    

    #Set e and n
    e = 3
    n = int(args.n)

    #Generate p such (p-1) is co-prime with e
    while True:
        p = number.getPrime(n) 
        if (p-1)%e:
            break

    #Generate q such (q-1) is co-prime with e
    while True:
        q = number.getPrime(n) 
        if (q-1)%e:
            break

    #Compute N and d
    N = p*q
    d = number.inverse(e, (p-1)*(q-1))

    #Open files
    public_file = open(args.p, 'w')
    private_file = open(args.s, 'w')

    #Write Public Key File
    public_file.write(str(2*n)+'\n')
    public_file.write(str(N)+'\n')
    public_file.write(str(e))

    #Write Private Key File
    private_file.write(str(2*n)+'\n')
    private_file.write(str(N)+'\n')
    private_file.write(str(d))

    #Close files
    public_file.close()
    private_file.close()