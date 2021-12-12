import socket

import os

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


def close():
    global obj
    obj.close()