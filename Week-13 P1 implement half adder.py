#Week-13 P1
#Write a program to implement half adder
def xor(bit_a, bit_b):
    a1 = bit_a and (not bit_b)
    a2 = (not bit_a) and bit_b
    return int(a1 or a2)
print("-----------------------")
print("XOR LOGIC OUTPUT")
print("Output of 0 XOR 0 is: ", xor(0,0))
print("Output of 0 XOR 1 is: ", xor(0,1))
print("Output of 1 XOR 0 is: ", xor(1,0))
print("Output of 1 XOR 1 is: ", xor(1,1))

def half_adder(bit_a, bit_b):
    return(xor(bit_a, bit_b), bit_a and bit_b)
print("------------------------")
print("HALF ADDER OUTPUT")
print("Output of (0,0) sum and carry is: ", half_adder(0,0))
print("Output of (0,1) sum and carry is: ", half_adder(0,1))
print("Output of (1,0) sum and carry is: ", half_adder(1,0))
print("Output of (1,1) sum and carry is: ", half_adder(1,1))
