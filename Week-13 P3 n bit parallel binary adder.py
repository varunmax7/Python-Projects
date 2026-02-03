#Week-13 P3
#Program: n bit parallel Binary adder
def n_bit_parallel_adder(a,b):
    carry = 0
    result =[]
    for i in range(len(a)-1, -1, -1):
        sum_bit = (a[i]^b[i])^carry
        carry = (a[i]&b[i])|(carry&(a[i]^b[i]))
        result.insert(0, sum_bit)
    if carry:
        result.insert(0, carry)
    return result
a = [1,0,1,1]
b = [0,1,1,0]
sum_result = n_bit_parallel_adder(a,b)
print(sum_result)
