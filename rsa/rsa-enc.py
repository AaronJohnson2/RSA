#import sys
#sys.path.append("lib")
import halib2
import math

if __name__ == "__main__":
    args = halib2.arg_return(0)    

    public_file = open(args.k, "r")    
    message_file = open(args.i, "r")

    size_N = int(public_file.readline())
    N = int(public_file.readline())
    e = int(public_file.readline())
    n = math.ceil(size_N/2)

    tmpM = message_file.read().replace('\n','')
    hexM = bytes.fromhex(tmpM)
    m = int.from_bytes(hexM, byteorder='big')
    print(m)
    #size_m = math.floor(math.log(m,2))+1
    size_m = len(hexM)*8
    print(size_m)