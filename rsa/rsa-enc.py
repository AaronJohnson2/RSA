#Students: Hayden Coffey, Aaron Johnson
#Course: COSC 483
#Project 2

from halib2_Electric_Boogaloo import arg_return, halib_pow
import math
import os

if __name__ == "__main__":
    #Read in cmd line arguments
    args = arg_return(0)    

    #Open files
    public_file = open(args.k, "r")    
    message_file = open(args.i, "r")
    cipher_file = open(args.o, 'w')

    #Read in public key data
    size_N = int(public_file.readline())
    N = int(public_file.readline())
    e = int(public_file.readline())
    n = math.ceil(size_N/2)

    #Read in message and convert to bytes
    tmpM = message_file.read().replace('\n','')
    hexM = bytes.fromhex(tmpM)
    size_m = len(hexM)*8
    #m = int.from_bytes(hexM, byteorder='big')

    #Verify message length
    if size_m > (n/2 - 24):
        print("Message too large for N")
        exit(0)

    #Generate random padding
    r = bytearray()
    count = 0
    while count < (n/8) - len(hexM) - 3:
        tmpByte = os.urandom(1)
        tmpInt = int.from_bytes(tmpByte, byteorder='big')

        if tmpInt != 0:
            r += tmpByte
            count+=1

    #Concatonation and message encryption 
    m_hat = int.from_bytes(bytes.fromhex('0002') + r + bytes.fromhex('00') + hexM, byteorder='big')
    c = halib_pow(m_hat,e,N)

    #Write cipher to file
    cipher_file.write(str(c))

    #Close files   
    message_file.close()
    public_file.close()
    cipher_file.close()