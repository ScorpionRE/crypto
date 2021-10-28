import urllib
print(urllib.quote("flag{1234_!@#$}"))
#unquote解码
d = {'name':'www@com','flag':'flag{1234_!@#$}'}
print(urllib.urlencode(d)) #urlencode能对字典模式的键值进行url编码

