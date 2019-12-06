#!/usr/bin/python
import sys

N = int(sys.argv[1])
Y = int(3)

def fn(n):
    if n !=0:
        print(n*' '+((N-n)*2+1)*'x') 
        fn(n-1)
    else:
        if (Y<=N):
            print(N*' '+'xx')
        else:
            print(N*' '+'x')
fn(int(sys.argv[1]))
