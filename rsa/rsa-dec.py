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
    print(m_hat)