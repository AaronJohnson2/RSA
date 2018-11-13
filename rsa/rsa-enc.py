#import sys
#sys.path.append("lib")
import halib2
import math
import os

if __name__ == "__main__":
    args = halib2.arg_return(0)    

    public_file = open(args.k, "r")    
    message_file = open(args.i, "r")
    cipher_file = open(args.o, 'w')

    size_N = int(public_file.readline())
    N = int(public_file.readline())
    e = int(public_file.readline())
    n = math.ceil(size_N/2)

    tmpM = message_file.read().replace('\n','')
    hexM = bytes.fromhex(tmpM)
    m = int.from_bytes(hexM, byteorder='big')
    #size_m = math.floor(math.log(m,2))+1
#    print(size_N)

    size_m = len(hexM)*8

#    print(size_m)

    #if size_m > (size_N - 2):
    if size_m > (size_N - 8):
        print("Invalid message size")
        exit(0)

    #print(os.urandom((size_m)/8 - 2))
    r = os.urandom(int((size_m)/8 - 1))
#    print(r)
#    print(hexM)

    m_hat = int.from_bytes(r + hexM, byteorder='big')
    c = pow(m_hat,e,N)

    cipher_file.write(str(c))
    
    print(m_hat)
    message_file.close()
    public_file.close()
    cipher_file.close()