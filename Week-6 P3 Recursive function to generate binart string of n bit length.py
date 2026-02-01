#Week-6 P3 Recursive function to generate binary string of n bit length
def genbin(n, bs=''):
    if len(bs)==n:
        print(bs)
    else:
        genbin(n, bs+'0')
        genbin(n, bs+'1')
genbin(2)
