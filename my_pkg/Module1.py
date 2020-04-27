#!/usr/bin/python
binary_num = int(input("input binary number : "))
exp = 1
DEC = 0
OCT = 0
HEX = 0

while(binary_num > 0):
	DEC = DEC + (binary_num % 10) * exp
	binary_num = binary_num // 10
	exp = exp * 2

OCT = format(DEC,'o')
HEX = format(DEC,'X')
print("=> OCT>",OCT)		
print("=> DEC>",DEC)
print("=> HEX>",HEX) 
	


