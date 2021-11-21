key = "whoami"
#flag = "00ba 8f11 2b22 9f51 a12f abb7 4bd7 3fef e1b5 13be c4d4 5d03 d900 7aca 1d51 a473 b5ef 3d9b 31b3"
with open('file.txt','rb') as f:
    flag = f.read()
s = ['']*256
t = ['']*256
f = ""
for i in range(256):
    s[i] = i
    t[i] = ord(key[i%(len(key))])
j = 0
for i in range(256):
    j = (j+s[i]+t[i] ) %256
    s[i],s[j] = s[j],s[i]
i = 0
j = 0
for m in range(38):
    i = (i+1)% 256
    j = (j + s[i]) %256
    s[i],s[j] = s[j],s[i]
    x = (s[i] + s[j] % 256)%256
    f+= chr(flag[m]^s[x])
print(f)