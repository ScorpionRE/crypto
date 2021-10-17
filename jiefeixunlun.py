#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
  
 
  
#秘钥
key="2,3,7,5,13,12,9,1,8,10,4,11,6"
#密文
cipher_text = "NFQKSEVOQOFNP"
  
  
f = open("1.txt")
str_first_encry = []
  
  
for line in f:
    line = line.strip()
    str_first_encry.append(line)
  

key_index = key.split(",")
str_second_encry=[]
for k in key_index:
    str_second_encry.append(str_first_encry[int(k)-1])
    print(str_first_encry[int(k)-1])
  
  
for i,ch in enumerate(cipher_text):
    line = str_second_encry[i]
    split_index = line.index(ch)
    temp=[]
    temp[0:len(line)-split_index+1] = line[split_index:len(line)]
    temp[len(temp):] = line[0:split_index]
    str_second_encry[i] = "".join(temp)
print("-------------------------------------")
for plain in str_second_encry:
    print(plain)



'''
按列输出
'''


for j in range(len(str_second_encry[0])):
    for i in range(13):
        line = str_second_encry[i]
        print(line[j].lower(),end = "")
    print("!")