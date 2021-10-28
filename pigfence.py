#猪圈变式，左右字母表相对应替换
if __name__ == '__main__':
    dic = {'a': 'j', 'b': 'k', 'c': 'l', 'd': 'm', 'e': 'n', 'f': 'o', 'g': 'p', 'h': 'q', 'i': 'r', 's': 'w', 'v': 'z',
           't': 'x', 'u': 'y', 'j': 'a', 'k': 'b', 'l': 'c', 'm': 'd', 'n': 'e', 'o': 'f', 'p': 'g', 'q': 'h', 'r': 'i',
           'w': 's', 'z': 'v', 'x': 't', 'y': 'u'}
    crypto = 'ocjp{zkirjwmo-ollj-nmlw-joxi-tmolnrnotvms}'
    plaintext = ''
    for c in crypto:
        if c in dic:
            plaintext += dic[c]
        else:
            plaintext += c
    print(plaintext)