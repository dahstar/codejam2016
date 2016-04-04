from stack import Stack
import math
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = long(decNumber) % long(base)
        remstack.push(rem)
        decNumber = long(decNumber )// long(base)

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString
print(baseConverter(long(math.pow(math.sqrt(5)+3,500000000)),10))