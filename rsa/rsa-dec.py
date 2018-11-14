#Students: Hayden Coffey, Aaron Johnson
#Course: COSC 483
#Project 2

import halib2_Electric_Boogaloo
import math

if __name__ == "__main__":
    #Read in cmd line arguments
    args = halib2_Electric_Boogaloo.arg_return(0)    

    #Open files
    private_file = open(args.k, "r")    
    cipher_file = open(args.i, "r")
    message_file = open(args.o, 'w')

    #Read in private key data
    size_N = int(private_file.readline())
    N = int(private_file.readline())
    d = int(private_file.readline())
    n = math.ceil(size_N/2)

    #Read in cipher text
    c = int(cipher_file.read())

    #Decrypt cipher text
    m_hat = pow(c, d, N)
    m_Bytes = bytes(m_hat.to_bytes(int(n/8), byteorder='big'))

    #Find end of padding
    zero_count = 0
    index = 0
    for byte in m_Bytes:
        if byte == 0:
            zero_count+=1
            if zero_count == 2:
                break
        index+=1

    #Remove padding    
    m = str((m_Bytes[index+1:]).hex())

    #Write message to file
    message_file.write(m + '\n')

    #Close files
    private_file.close()
    cipher_file.close()
    message_file.close()