print("Decimal to binary")
a = 88
print(a)
b = bin(88)
print(b)
print()

print("Binary to decimal")
a = '0b1011000'
print(a)
b = int('0b1011000', 2)
print(b)
print()

print("Bitwise AND")
a = 0b01100000
b = 0b00100110
print(bin(a & b))
# 0b100000
print()

print("Bitwise OR")
a = 0b01100000
b = 0b00100110
print(bin(a | b))
# 0b1100110
print()

print("Bitwise XOR")
a = 0b01100000
b = 0b00100110
print(bin(a ^ b))
# 0b1000110
print()

print("Shift right")
print(bin(a))
print(bin(a >> 2))
print()

print("Shift left")
print(bin(a))
print(bin(a << 1))
