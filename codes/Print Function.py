from __future__ import print_function

if __name__ == '__main__':
    a = []
    n = int(raw_input())
    for i in range (1,n+1):
        a.append (i)
    print (''.join(str(j) for j in a))
