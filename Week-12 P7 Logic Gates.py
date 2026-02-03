#Week-12 P7
#Logic GATES
#AND GATE
def AND(a, b):
    return a&b
print("AND LOGIC OUTPUT")
print("Output of 0&0 is: ", AND(0, 0))
print("Output of 0&1 is: ", AND(0, 1))
print("Output of 1&0 is: ", AND(1, 0))
print("Output of 1&1 is: ", AND(1, 1))

#OR GATE
def OR(a, b):
    return a|b
print("OR LOGIC OUTPUT")
print("Output of 0 and 0 is: ", OR(0, 0))
print("Output of 0 and 1 is: ", OR(0, 1))
print("Output of 1 and 0 is: ", OR(1, 0))
print("Output of 1 and 1 is: ", OR(1, 1))

#NOT GATE
def NOT(a):
    return ~a+2
print("NOT LOGIC OUTPUT")
print("Output of NOT for 0 is: ", NOT(0))
print("Output of NOT for 1 is: ", NOT(1))

#XOR GATE
def XOR(a, b):
    return a^b
print("XOR LOGIC OUTPUT")
print("Output of 0 XOR 0 is: ", XOR(0, 0))
print("Output of 0 XOR 1 is: ", XOR(0, 1))
print("Output of 1 XOR 0 is: ", XOR(1, 0))
print("Output of 1 XOR 1 is: ", XOR(1, 1))
















