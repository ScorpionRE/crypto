from pwn import remote

p = remote("175.178.248.28", 10086)

ATTEMPTS = 10
import conn
def attempt(i):
    print(p.recvline())
    powstr = p.recvline()
    p.sendline(conn.POW(powstr))
    p.sendline(1)
    p.sendline("P"*i)
    p.recvline()
    return len(p.recvline()[:-1])//2
    # NOTE: response is in hexadecimal format, two digits for each byte

minimum_length = min([attempt(0) for j in range(ATTEMPTS)]) - 16

i=1
while True:
    length = min([attempt(i) for j in range(ATTEMPTS)]) - 16
    if length>minimum_length:
        print("Length: {} bytes".format(length-i))
        break
    i+=1
p.sendline('q')