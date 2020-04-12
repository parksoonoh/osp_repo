#!/usr/bin/python

N = int(input('N : '))
S = 0

for i in range(N):
   num = int(input('number : '))
   S = S + num

print('the average of number :',float(S/N))

