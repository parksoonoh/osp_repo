#!/usr/bin/python

N = int(input('fibonacci number? '))
A = 1
B = 1
temp = 0;
for i in range(N):
   if i < 2:
      A = 1
   else:
      temp = B
      B = A + B
      A = temp
   if i == N - 1:
      print(B)
   else : 
      print(B, end = ',')
print('F',N,' = ',B)
