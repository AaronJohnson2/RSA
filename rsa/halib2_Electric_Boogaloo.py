#Students: Hayden Coffey, Aaron Johnson
#Course: COSC 483
#Project 2
import argparse
import os

from Crypto.Random import random
#Return argument datastructure for specified process


def arg_return(mode):
    #Encryption / Decryption Function Mode
    if not mode:
        parser = argparse.ArgumentParser(
            description='Encrypt/Decrypt integer with RSA.')
        parser.add_argument('-k', help="Key file.")
        parser.add_argument('-i', help="Input file.")
        parser.add_argument('-o', help="Output file.")

        args = parser.parse_args()

        if args.k == None or args.i == None or args.o == None:
                parser.print_help()
                exit()

        return args

    #RSA keygen mode
    else:
        parser = argparse.ArgumentParser(
            description='Generate private/public RSA keys.')
        parser.add_argument('-p', help="Public key file.")
        parser.add_argument('-s', help="Secret key file.")
        parser.add_argument('-n', help="Number of bits.")

        args = parser.parse_args()

        if args.p == None or args.s == None or args.n == None:
                parser.print_help()
                exit()

        return args

#Implemented via Successive Squaring technique, b^e % m
def halib_pow(b, e, m):
    #Convert exponent to binary
    binE = '{0:08b}'.format(e)

    #Find powers of 2 corresponding to each bit equal to 1
    two_powers = []
    count = 0
    for bit in binE[::-1]:
        if int(bit) == 1:
            two_powers.append(count)
        count+=1

    #Compute successive squares up to most significant power of 2
    raised_values = []
    raised_values.append(b%m)
    for i in range(1,two_powers[-1]+1):
        raised_values.append((raised_values[i-1]**2)%m)

    #Compute product of needed squares
    product = 1
    for i in two_powers:
        product *= raised_values[i]

    #Return answer
    return product%m

#Returns random prime of specified bit length via Fermat's Probabilistic Prime Test
def halib_getprime(bits):
    #Threshold for number of a's to check
    theta = 5 

    #Initial candidate
    n = random.randrange(2**(bits-1), 2**bits-1)
    print(n)
    #Perform prime test
    count = 0
    while count < theta:
        a = random.randrange(2, n-1)
        tmp = halib_pow(a,n-1,n) 
        count += 1

        if tmp != 1:
            n = random.randrange(2**(bits-1), 2**bits-1)
            print(n)
            count = 0

    return n