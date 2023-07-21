#CRC working simulation
#logic
import math
def XOR(a, b):
    return a != b
def AND(a, b):
    return a * b
def OR(a, b):
    return int(bool(a + b))
#fulladder
def full_adder(x, y, cin):
    sum = XOR(XOR(x, y), cin)
    cout = OR(OR(AND(x, y), AND(y, cin)), AND(x, cin))
    return (sum, cout)
def binary_adder(x, y, cin=0):
    l = len(x)
    sum = ""
    carry = cin
    for i in range(l - 1, -1, -1):
        bit_sum, carry = full_adder(int(x[i]), int(y[i]), carry)
        sum = str(int(bit_sum)) + sum
    return sum
#compliment 2s
def twos_complement(y):
    # leave all least significant 0's and first 1 unchanged,
    # and, replace 1's by 0's and 0's by 1's in all other higher significant bits
    n = len(y)
    i = n - 1
    y1 = ""
    for i in range(n - 1, -1, -1):
        y1 = y[i] + y1
        if y[i] == "1":
            i = i - 1  # first 1 found gives eg XX100
            break
        i = i - 1
    while i >= 0:#flips remaining set of numbers
        if y[i] == "0":
            y1 = "1" + y1
        else:
            y1 = "0" + y1
        i = i - 1
    return y1
#division
def restoring_division(Q, M):
    count = len(Q)  # no of bits in dividend Q
    if len(M) <= count:
        M = M.zfill(count + 1)
    M_comp = twos_complement(M)
    # initialize accumulator with zero
    A = "0" * len(M)

    for i in range(count):
        # Left shift A, Q
        A = A[1:] + Q[0]
        Q = Q[1:]  # one bit is less, which is empty

        # A <- A - M
        A = binary_adder(A, M_comp)

        if A[0] == "1":
            # Set Qo to 0
            Q = Q + "0"
            # A <- A + M (restore A)
            A = binary_adder(A, M)
        else:
            # Set Qo to 1
            Q = Q + "1"

    return (Q, A)

def numConcat(num1, num2):
     # Convert both the numbers to
        # strings
     num1 = str(num1)
     num2 = str(num2)
         
        # Concatenate the strings
     num1 += num2
     
     return int(num1)
if __name__ == "__main__":
    print("Senderr:")
    Q = input("Enter data: ")
    q=Q
    q=str(q)
    M ="1001"

    count=len(M)-1
    rd="0"
    rd= rd.zfill(count)
    q=str(numConcat(q,rd))

    #print(q)
    if int(q) < int(M):
        quotient, remainder = "0" * len(q), q
    else:
        quotient, remainder = restoring_division(q, M)
   # print(quotient,"\t",remainder)
   
    cws=str(numConcat(Q,remainder))
    print("Code Word from Source :")
    print(cws)
    print("Sending.......\n")
    print("Sending.......\n")
    print("Sending.......\n")
    print("Sending.......\n")
    print("Sending.......\n")
    print("Sending.......\n")

    print("Receiver:")
    while True:
     cw=input("Enter receiver code:")
     M ="1001"
     if int(cw) < int(M):
         dw, rem = "0" * len(cw), cw
     else:
         dw, rem = restoring_division(cw, M)
     print("The Received Code word is ")
     print(cw)
     print("Data is ")
     l=len(remainder)
     print(cw[:-l])
     print(cw)
   # print(dw)
     print(rem)
     if int(rem)==0:
         print("It is correct")
         break
     else:
         print("ARQ")   