import halib2
import math
from Crypto.Util import number

if __name__ == "__main__":
    args = halib2.arg_return(1)    

    e = 3
    n = int(args.n)

    while True:
        p = number.getPrime(n) 
        if (p-1)%e:
            break

    while True:
        q = number.getPrime(n) 
        if (q-1)%e:
            break
    N = p*q
    d = number.inverse(e, (p-1)*(q-1))

    public_file = open(args.p, 'w')
    private_file = open(args.s, 'w')

    #Public File
    #public_file.write(str(math.floor(math.log(N, 2))+1)+'\n')
    public_file.write(str(2*n)+'\n')
    public_file.write(str(N)+'\n')
    public_file.write(str(e))

    #Private File
    #private_file.write(str(math.floor(math.log(N,2))+1)+'\n')
    private_file.write(str(2*n)+'\n')
    private_file.write(str(N)+'\n')
    private_file.write(str(d))

    public_file.close()
    private_file.close()