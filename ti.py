from Crypto.Util.number import long_to_bytes

with open("chall.txt",'r') as f:
    m = f.readlines()

flag = ""
for i in range(len(m)):
    m[i] = m[i].strip("\n")
    flag += bin(int(m[i]))[-1]

print(long_to_bytes(int(flag,2)))
print(long_to_bytes(int(flag[::-1],2)))