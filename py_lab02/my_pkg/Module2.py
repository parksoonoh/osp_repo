#!/usr/bin/python

import re

inter = []
union = []
list1 = input("1st list : ")
list2 = input("2nd list : ")
list1_num = re.findall("\d+",list1)
list2_num = re.findall("\d+",list2)
for i in range(len(list1_num)):
	for j in range(len(list2_num)):
		if(list1_num[i] == list2_num[j]):
			inter.append(list1_num[i])
for i in range(len(list1_num)):
	count = 0
	for j in range(len(inter)):
		if(list1_num[i] == inter[j]):
			count = count + 1
	if(count == 0):
		union.append(list1_num[i])
for i in range(len(list2_num)):
	count = 0
	for j in range(len(inter)):
		if(list2_num[i] == inter[j]):
			count = count + 1
	if(count == 0):
		union.append(list2_num[i])
union.extend(inter)
inter.sort()
union.sort()
inter = list(map(int,inter))
union = list(map(int,union))
print("=> union [", end = "")
for i in range(len(union)):
	if(i == len(union) - 1):
		print(union[i], end = "")
	else:
		print(union[i], end = ",")
print("]")
		
print("=> inter [", end = "")
for i in range(len(inter)):
	if(i == len(inter) - 1):
		print(inter[i], end = "")
	else:
		print(inter[i], end = ",")
print("]")


