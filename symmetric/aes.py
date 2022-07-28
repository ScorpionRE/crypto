from pwn import *
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from hashlib import md5
from datetime import datetime
from time import time
from parse import parse
#from multiprocessing import Pool

def oracle_encrypt(conn, pt):
    conn.sendlineafter('> ', '1')
    conn.sendlineafter('your plaintext(hex): ', pt.hex())
    l = conn.recvline().decode()
    r = parse("here's the ciphertext: {}:{}:{}\n", l)
    return [bytes.fromhex(x) for x in r] # iv1, iv2, ct

def oracle_decrypt(conn, iv1, iv2, ct):
    conn.sendlineafter('> ', '2')
    pl = f'{iv1.hex()}:{iv2.hex()}:{ct.hex()}'
    conn.sendlineafter('your ciphertext: ', pl)
    l = conn.recvline().decode()
    pt = parse("here's the plaintext(hex): {}\n", l)
    return bytes.fromhex(pt[0])

def get_flag(conn):
    conn.sendlineafter('> ', '3')
    l = conn.recvline().decode()
    r = parse("here's the encrypted flag: {}:{}:{}\n", l)
    return [bytes.fromhex(x) for x in r] # iv1, iv2, ct

def go(attempt):
    start = time()
    print('[!] starting attempt', attempt)
    conn = remote('crypto.ctf.zer0pts.com', 10929, level='error')
    KNOWN_PT = b'a'*16
    KNOWN_IV1, KNOWN_IV2, KNOWN_CT = oracle_encrypt(conn, KNOWN_PT)

    RAND_IV2 = b'\x77'*16
    for k in range(256**2):
        key3 = int.to_bytes(k, 3, 'big')
        key = md5(key3).digest()
        cipher = AES.new(key=key, mode=AES.MODE_ECB)
        E_R_IV2 = cipher.encrypt(RAND_IV2)
        E_IV2 = cipher.encrypt(KNOWN_IV2)
        C_to_send = strxor(KNOWN_CT, strxor(E_IV2, E_R_IV2))
        pt = oracle_decrypt(conn, KNOWN_IV1, RAND_IV2, C_to_send)
        if pt == KNOWN_PT:
            win_msg = f'===== ATTEMPT {attempt} ======\n'
            win_msg += f'[+] key3 found: {key3.hex()}\n'
            win_msg += f'[+] KNOWN_PT: {KNOWN_PT.hex()}\n'
            win_msg += f'[+] KNOWN_IV1: {KNOWN_IV1.hex()}\n'
            win_msg += f'[+] KNOWN_IV2: {KNOWN_IV2.hex()}\n'
            win_msg += f'[+] KNOWN_CT: {KNOWN_CT.hex()}\n'
            FLAG_IV1, FLAG_IV2, FLAG_CT = get_flag(conn)
            win_msg += f'[+] FLAG_IV1: {FLAG_IV1.hex()}\n'
            win_msg += f'[+] FLAG_IV2: {FLAG_IV2.hex()}\n'
            win_msg += f'[+] FLAG_CT: {FLAG_CT.hex()}\n'
            print(win_msg)
            with open('./win-'+str(attempt), 'w') as f:
                f.write(win_msg)
            return True
    took = time() - start

    conn.close()
    return False


def pre_num(ps):
    with open(ps,'r') as f:
        ps = f.readlines()
    s = []
    for i in range(len(ps)):
        ps[i] = int(ps[i].strip('\n'))
        num = bin(ps[i])[2:].rfind('1')
        s.append(num)
    print(s)
    return ps,s

def find_choose(r,s,ps):
    with open(r,'r') as f:
        r = int(f.read())
    m = list('0'*512)  #bchoose

    for i in range(512):
        if (r>>i) % 2 == 0:
            m[s.index(511-i)] = '0'
        else:
            r = r^ps[s.index(511-i)]
            m[s.index(511-i)] = '1'

    choose = int("0b" + "".join(m), 2)
    print(choose)
    return choose

def sm():
    ps,s = pre_num("ps")
    print(ps)
    choose = find_choose("r",s,ps)
    key = long_to_bytes(int(hashlib.md5(long_to_bytes(choose)).hexdigest(), 16))
    aes_obj = AES.new(key, AES.MODE_ECB)
    f2 = open("ef", "rb")
    ef = f2.read()
    ef = base64.b64decode(ef)
    result = aes_obj.decrypt(ef)
    print(result)


if __name__ == "__main__":
    key = sm()
