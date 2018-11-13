import argparse

#Return argument datastructure for specified process
def arg_return(mode):
    #Encryption / Decryption Function Mode
    if not mode:
        parser = argparse.ArgumentParser(description='Encrypt/Decrypt integer with RSA.')
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
        parser = argparse.ArgumentParser(description='Generate private/public RSA keys.')
        parser.add_argument('-p', help="Public key file.")
        parser.add_argument('-s', help="Secret key file.")
        parser.add_argument('-n', help="Number of bits.")

        args = parser.parse_args()

        if args.p == None or args.s == None or args.n == None:
                parser.print_help()
                exit()

        return args

#l function
def l(n):
        return 2*n - 4