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

    size_m = len(hexM)*8

    if size_m > (n/2 - 24):
        print("Invalid message size")
        exit(0)

    r = bytearray()
    count = 0
    while count < (n/8) - len(hexM) - 3:
        tmpByte = os.urandom(1)
        tmpInt = int.from_bytes(tmpByte, byteorder='big')

        if tmpInt != 0:
            r += tmpByte
            count+=1

    m_hat = int.from_bytes(bytes.fromhex('0002') + r + bytes.fromhex('00') + hexM, byteorder='big')
    c = pow(m_hat,e,N)

    cipher_file.write(str(c))
    
    message_file.close()
    public_file.close()
    cipher_file.close()