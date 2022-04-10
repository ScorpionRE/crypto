import socket
import re
import os
import hash
obj = None


def remote(addr, ip):
    global obj
    obj = socket.socket()
    obj.connect((addr, ip))


def reads():
    global obj
    ret_bytes = obj.recv(1024)
    ret_str = str(ret_bytes, encoding="utf-8")
    # print(ret_str)
    return ret_str


def sends(content):
    global obj
    obj.sendall(bytes(content + "\n", encoding="utf-8"))

def get_m(str):
    return str.split(b'==')[1].strip(b'\n')

def get_flag(str):
    tmp = str.split(b'+')[1]
    m = tmp.split(b')')[0]
    return m

def POW(str):
    m = str(get_m(str),encodings = "utf-8")
    flag = str(get_flag(str),encodings = "utf-8")
    return hash.brute_sha256(flag,m)




def close():
    global obj
    obj.close()