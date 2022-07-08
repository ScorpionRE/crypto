from hashlib import sha256
from pwn import *
from pwnlib.util.iters import mbruteforce

def proof_of_work(p):
    p.recvuntil("XXXX+")
    suffix = p.recv(16)
    p.recvuntil(" == ")
    cipher = p.recvline().strip().decode("utf8")
    proof = mbruteforce(lambda x: sha256((x + suffix).encode()).hexdigest() ==
                        cipher, string.ascii_letters + string.digits, length=3, method='fixed')
    p.sendlineafter("Give me XXX:", proof)
    p.recvline()


if __name__ == "__main__":
    # io = remote('123.56.111.202', 38428)
    # proof_of_work(io)
    print('0'*128)
