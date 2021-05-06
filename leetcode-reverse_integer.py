#Given a signed 32-bit integer x, return x with its digits reversed. If reversing 
#x causes the value to go outside the signed 32-bit
# integer range [-231, 231 - 1], then return 0
#test data : Input: x = 123 Output: 321 , Input: x = -123 Output: -321 , Input: x = 120 Output: 21
# Input: x = 123 Output: 321


def reverse(x :int) -> int:
# reverses the integer that has been input

    rev = int(str(abs(x))[::-1])
    if rev.bit_length() <32 :
        return (-rev if x<0 else rev)
    else :
        return 0
        
a = reverse(123)
print(a)
a = reverse(-123)
print(a)
a = reverse(120)
print(a) # an integer cannot have 0 at the start.
a = reverse(0)
print(a)