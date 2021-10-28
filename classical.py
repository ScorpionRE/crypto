#古典密码
#简单移位密码
'''
m,k
以k的长度l切分m
明文字符位置1234
密文字符位置3124（如把第一个字符放到第三个去）
'''

def shift_encrypt(m,k):
	l = len(k)
	c = ""
	for i in range(0,len(m),l):
		tmp_c = [""]*l
		if i + 1 > len(m):
			tmp_m = m[i:]
		else:
			tmp_m = m[i:i+l]
		for kidx in range(len(tmp_m)):
			tmp_c[int(k[kidx]) - 1] = tmp_m[kidx]
		c += "".join(tmp_c)
	return c

def shift_decrypt(c,k):
	l = len(k)
	m = ""
	for i in range(0,len(c),l):
		tmp_m = [""] * l
		if i + l >= len(c):
			tmp_c = c[i:]
			use = []
			for kidx in range(len(tmp_c)):
				use.append(int(k[kidx]) - 1)
			use.sort()
			for kidx in range(len(tmp_c)):
				tmp_m[kidx] = tmp_c[use.index(int(k[kidx])-1)]

		else:
			tmp_c = c[i:i+l]
			for kidx in range(len(tmp_c)):
				tmp_m[kidx] = tmp_c[int(k[kidx]) - 1]

		m += "".join(tmp_m)

	return m

#云影密码

def c01248_decode(c):
	l=c.split("0")
	origin = "abcdefghijklmnopqrstuvwxyz"
	r = ""
	for i in l:
		tmp = 0
		for num in i:
			tmp += int(num)
			r += origin[tmp-1]
	return r

'''
栅栏密码


'''
if __name__ == '__main__':
	m = "flag{easy_easy_crypto}"
	k = "3124"
	c = shift_encrypt(m,k)
	print(c)
	n = shift_decrypt(c,k)
	print(n)