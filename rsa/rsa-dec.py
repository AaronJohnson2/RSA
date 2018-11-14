import halib2
import math

if __name__ == "__main__":
    args = halib2.arg_return(0)    

    private_file = open(args.k, "r")    
    cipher_file = open(args.i, "r")
    message_file = open(args.o, 'w')

    size_N = int(private_file.readline())
    N = int(private_file.readline())
    d = int(private_file.readline())
    n = math.ceil(size_N/2)

    c = int(cipher_file.read())
    m_hat = pow(c, d, N)

    m_Bytes = bytes(m_hat.to_bytes(int(n/8), byteorder='big'))

    zero_count = 0
    index = 0
    for byte in m_Bytes:

        if byte == 0:
            zero_count+=1

            if zero_count == 2:
                break

        index+=1
    
    m = str((m_Bytes[index+1:]).hex())

    message_file.write(m + '\n')

    private_file.close()
    cipher_file.close()
    message_file.close()
    #print(m_hat)