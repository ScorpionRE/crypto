#古典密码
#简单移位密码
import base64
import binascii
import codecs
import string

'''
m,k
以k的长度l切分m
明文字符位置1234
密文字符位置3124（如把第一个字符放到第三个去）
'''
#
# def shift_encrypt(m,k):
#     l = len(k)
#     c = ""
#     for i in range(0,len(m),l):
#         tmp_c = [""]*l
#         if i + 1 > len(m):
#             tmp_m = m[i:]
#         else:
#             tmp_m = m[i:i+l]
#         for kidx in range(len(tmp_m)):
#             tmp_c[int(k[kidx]) - 1] = tmp_m[kidx]
#         c += "".join(tmp_c)
#     return c
#
# def shift_decrypt(c,k):
#     l = len(k)
#     m = ""
#     for i in range(0,len(c),l):
#         tmp_m = [""] * l
#         if i + l >= len(c):
#             tmp_c = c[i:]
#             use = []
#             for kidx in range(len(tmp_c)):
#                 use.append(int(k[kidx]) - 1)
#             use.sort()
#             for kidx in range(len(tmp_c)):
#                 tmp_m[kidx] = tmp_c[use.index(int(k[kidx])-1)]
#
#         else:
#             tmp_c = c[i:i+l]
#             for kidx in range(len(tmp_c)):
#                 tmp_m[kidx] = tmp_c[int(k[kidx]) - 1]
#
#         m += "".join(tmp_m)
#
#     return m
#
# #云影密码
#
# def c01248_decode(c):
#     l=c.split("0")
#     origin = "abcdefghijklmnopqrstuvwxyz"
#     r = ""
#     for i in l:
#         tmp = 0
#         for num in i:
#             tmp += int(num)
#             r += origin[tmp-1]
#     return r

#xor
# a = 'lovelovelovelovelovelovelovelove'
# b = [0x0A,0x03,0x17,0x02,0x56,0x01,0x15,0x11,0x0A,0x14,0x0E,0x0A,0x1E,0x30,0x0E,0x0A,0x1E,0x30,0x0E,0x0A,0x1E,0x30,0x14,0x0C,0x19,0x0D,0x1F,0x10,0x0E,0x06,0x03,0x00]
#
# c = ''
# for i in range(len(a)):
#     c += chr(ord(a[i])^b[i])
# print(c)

#"凯撒密码解密")
#密文
# str = 'R5UALCUVJDCGD63RQISZTBOSO54JVBORP5SAT2OEQCWY6CGEO53Z67L'
# #密钥(平移位数)
# m = ''
# for my in range(1,26):
#     print("密钥",my)
#     for i in str:
#       mw = ord(i)
#       if (64 < mw < 91):#大写字母
#         jm = mw + my
#         if jm > 90:
#               jm = (mw - 26) + my
#               m += chr(jm)
#           #m.join(chr(jm))
#           #print(chr(jm), end='')
#         else:
#             m += chr(jm)
#           #print(chr(jm), end='')
#       elif (96 < mw < 123):#小写字母
#         jm = mw + my
#         if jm > 122:
#             jm = (mw - 26) + my
#             m += chr(jm)
#           #print(chr(jm), end='')
#         else:
#             m += chr(jm)
#           #print(chr(jm), end='')
#       else:#数字和特殊字符不做修改
#         jm = mw + 0
#         m += chr(jm)
#         #print(chr(jm), end='')
#     print(m)
#     try:
#         print(base64.b32decode(m))
#     except binascii.Error:
#         missing_padding = 2 - len(m) % 2  #base64为4
#         if missing_padding:
#             m += '=' * missing_padding
#         print(base64.b32decode(m))
#     m = ''
#

#polybius
# import itertools
#
# key = []
# cipher = "ouauuuoooeeaaiaeauieuooeeiea"
#
# for i in itertools.permutations('aeiou', 5):
#     key.append(''.join(i))
#
# for now_key in key:
#     solve_c = ""
#     res = ""
#     for now_c in cipher:
#         solve_c += str(now_key.index(now_c))
#     for i in range(0,len(solve_c),2):
#         now_ascii = int(solve_c[i])*5+int(solve_c[i+1])+97
#         if now_ascii>ord('i'):
#             now_ascii+=1
#         res += chr(now_ascii)
#     if "flag" in res:
#         print(now_key, res)


#移位
# fib = ""
#
# f =   ""
#
# c = "喵汪哞叽双哇顶，眠鸟足屁流脑，八哇报信断流脑全叽，眠鸟进北脑上草，八枝遇孙叽，孙叽对熬编叶：值天衣服放鸟捉猴顶。鸟对：北汪罗汉伏熬乱天门。合编放行，卡编扯呼。人离烧草，报信归洞，孙叽找爷爷。"
#
# m = ['']*32
#
# fib = fib.split('')
# f = f.split('')
# print(fib)
#
# for i in range(len(f)):
#     m[fib.index(f[i])] = c[i]
# for i in m:
#     print(i,end='')


#四方密码
# import collections
# import re
#
# matrix = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
# pla = 'abcdefghijklmnoprstuvwxyz'
# key1 = '[SECURITY]'
# key2 = '[INFORMATION]'
# key1 = ''.join(collections.OrderedDict.fromkeys(key1))
# key2 = ''.join(collections.OrderedDict.fromkeys(key2))
#
# matrix1 = re.sub('[\[\]]', '', key1) + re.sub(key1, '', matrix)
# matrix2 = re.sub('[\[\]]', '', key2) + re.sub(key2, '', matrix)
#
# matrix_list1 = []
# matrix_list2 = []
# pla_list = []
# for i in range(0, len(matrix1), 5):
#     matrix_list1.append(list(matrix1[i:i + 5]))
# # print matrix_list1
#
# for i in range(0, len(matrix2), 5):
#     matrix_list2.append(list(matrix2[i:i + 5]))
# # print matrix_list2
#
# for i in range(0, len(pla), 5):
#     pla_list.append(list(pla[i:i + 5]))
#
#
# # print pla_list
#
# # 查询两个密文字母位置
# def find_index1(x):
#     for i in range(len(matrix_list1)):
#         for j in range(len(matrix_list1[i])):
#             if matrix_list1[i][j] == x:
#                 return i, j
#
#
# def find_index2(y):
#     for k in range(len(matrix_list2)):
#         for l in range(len(matrix_list2[k])):
#             if matrix_list2[k][l] == y:
#                 return k, l
#
#
# def gen_pla(letter):
#
#
# # 两个子母中第一个字母位置
#     first = find_index1(letter[0])
#
# # 两个子母中第二个字母位置
#     second = find_index2(letter[1])
#
#     pla = ''
#     pla += pla_list[first[0]][second[1]]
#     pla += pla_list[second[0]][first[1]]
#
#     return pla
#
#
# def main():
#     cip = 'ZHNJINHOOPCFCUKTLJ'
#
#
#     pla = ''
#     for i in range(0, len(cip), 2):
#         pla += gen_pla(cip[i:i + 2])
#     print(pla)
#
# if __name__ == '__main__':
#     main()


#hill 希尔密码
# s='wznqcaduqopfkqnwofDbzgeu'
# #未给密钥的自己猜测
# flag_pre='utflag'
# def getit(a1,b1,c1,a2,b2,c2,a3,b3,c3):
#     for i in range(26):
#         for j in range(26):
#             if (a1 * i + b1 * j) % 26 == c1 and (a2 * i + b2 * j) % 26 == c2 and (a3 * i+b3*j) % 26 == c3:
#                 return (i,j)
# x1=getit(22,25,20,13,16,5,2,0,0)
# x2=getit(22,25,19,13,16,11,2,0,6)
# import string
# flag=''
# for i in range(0, len(s),2):
#     flag+=string.ascii_letters[(x1[0]*string.ascii_letters.index(s[i])+x1[1]*string.ascii_letters.index(s[i+1]))%26]
#     flag+=string.ascii_letters[(x2[0]*string.ascii_letters.index(s[i])+x2[1]*string.ascii_letters.index(s[i+1]))%26]
# print(flag)

#培根密码
# letters1 = [
#     'A', 'B', 'C', 'D', 'E', 'F', 'G',
#     'H', 'I', 'J', 'K', 'L', 'M', 'N',
#     'O', 'P', 'Q', 'R', 'S', 'T',
#     'U', 'V', 'W', 'X', 'Y', 'Z',
# ]
# letters2 = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g',
#     'h', 'i', 'j', 'k', 'l', 'm', 'n',
#     'o', 'p', 'q', 'r', 's', 't',
#     'u', 'v', 'w', 'x', 'y', 'z',
# ]
# cipher1 = [
#     "aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba",
#     "aabbb", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab",
#     "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb",
#     "babaa", "babab", "babba", "babbb", "bbaaa", "bbaab",
# ]
# cipher2 = [
#     "AAAAA", "AAAAB", "AAABA", "AAABB", "AABAA", "AABAB", "AABBA",
#     "AABBB", "ABAAA", "ABAAA", "ABAAB", "ABABA", "ABABB", "ABBAA",
#     "ABBAB", "ABBBA", "ABBBB", "BAAAA", "BAAAB", "BAABA",
#     "BAABB", "BAABB", "BABAA", "BABAB", "BABBA", "BABBB",
# ]
#
#
# def bacon1(string):
#     lists = []
#     # 分割，五个一组
#     for i in range(0, len(string), 5):
#         lists.append(string[i:i+5])
#     # print(lists)
#     # 循环匹配，得到下标，对应下标即可
#     for i in range(0, len(lists)):
#         for j in range(0, 26):
#             if lists[i] == cipher1[j]:
#                 # print(j)
#                 print(letters1[j], end="")
#     print("")
#
#
# def bacon2(string):
#     lists = []
#     # 分割，五个一组
#     for i in range(0, len(string), 5):
#         lists.append(string[i:i+5])
#     # print(lists)
#     # 循环匹配，得到下标，对应下标即可
#     for i in range(0, len(lists)):
#         for j in range(0, 26):
#             if lists[i] == cipher2[j]:
#                 # print(j)
#                 print(letters2[j], end="")
#     print("")
#
#
# bacon2("AABABABABAAAAAAAABBAABAAABAABAAABABABAAAABAABAABABABAABABAABB")


#猪圈变式，左右字母表相对应替换
# if __name__ == '__main__':
#     dic = {'a': 'j', 'b': 'k', 'c': 'l', 'd': 'm', 'e': 'n', 'f': 'o', 'g': 'p', 'h': 'q', 'i': 'r', 's': 'w', 'v': 'z',
#            't': 'x', 'u': 'y', 'j': 'a', 'k': 'b', 'l': 'c', 'm': 'd', 'n': 'e', 'o': 'f', 'p': 'g', 'q': 'h', 'r': 'i',
#            'w': 's', 'z': 'v', 'x': 't', 'y': 'u'}
#     crypto = 'ocjp{zkirjwmo-ollj-nmlw-joxi-tmolnrnotvms}'
#     plaintext = ''
#     for c in crypto:
#         if c in dic:
#             plaintext += dic[c]
#         else:
#             plaintext += c
#     print(plaintext)

#词频分析
#爆破密钥长度
    #找子串（长度3-4），爆破，（应该还有别的找最大字串算法）
# cipher = ""
# sub_str = []
# for i in range(26):
#     sub_str[0] = chr(ord('a')+i)
#     for j in range(26):
#         sub_str[1] = chr(ord('a')+j)
#         for k in range(26):
#             sub_str[2] = chr(ord('a') + k)
#             for l in range(26):
#                 sub_str[3] = chr(ord('a')+l)
#                 if cipher.count("".join(sub_str)) > 20:
#                     key = sub_str
#                     print(key)
#                     break
#     #找第i次出现的位置（下标j）
# def get_position(s,sub_s,i):





#rot

# a="83 89 78 84 45 86 96 45 115 121 110 116 136 132 132 132 108 128 117 118 134 110 123 111 110 127 108 112 124 122 108 118 128 108 131 114 127 134 108 116 124 124 113 108 76 76 76 76 138 23 90 81 66 71 64 69 114 65 112 64 66 63 69 61 70 114 62 66 61 62 69 67 70 63 61 110 110 112 64 68 62 70 61 112 111 112"
# b=a.split(" ")
# m="38e4c352809e150186920aac37190cbc"
# flag=""
# for j in range(0,26):
#     flag=""
#     for i in range(len(b)):
#         flag+=chr(int(b[i])-j)
#     print(flag)
#
#
#
# #杰斐逊轮
# # 秘钥
# key = "2,3,7,5,13,12,9,1,8,10,4,11,6"
# # 密文
# cipher_text = "NFQKSEVOQOFNP"
#
# f = open("1.txt")
# str_first_encry = []
#
# for line in f:
#     line = line.strip()
#     str_first_encry.append(line)
#
# key_index = key.split(",")
# str_second_encry = []
# for k in key_index:
#     str_second_encry.append(str_first_encry[int(k) - 1])
#     print(str_first_encry[int(k) - 1])
#
# for i, ch in enumerate(cipher_text):
#     line = str_second_encry[i]
#     split_index = line.index(ch)
#     temp = []
#     temp[0:len(line) - split_index + 1] = line[split_index:len(line)]
#     temp[len(temp):] = line[0:split_index]
#     str_second_encry[i] = "".join(temp)
# print("-------------------------------------")
# for plain in str_second_encry:
#     print(plain)
#
# '''
# 按列输出
# '''
#
# for j in range(len(str_second_encry[0])):
#     for i in range(13):
#         line = str_second_encry[i]
#         print(line[j].lower(), end="")
#     print("!")


#简单替换
def replacement(s,cipher):
    # s为m中对应的字母
    m = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    x = string.ascii_letters.maketrans(s, m)
    print(cipher.translate(x))


s="ojqdocpsnyumybdbnrlzfrdpxndsxzvlswdbkizubxaknlruifrclzvlbrqkmnmvruifdljpxeybqaqjtvldnnlbrrplpuniiydcqfysnerwvnqvkpxeybqbgwuasilqwempmjjvldbddsvhhmiwkdkjqdruifieddmnwzddejflxzvlswdzxxruxrlirduvnjqdmrhgtukkhgrlszjlqwjrhjqdnzhgrssnhhdcobqytybggxwekdpjqdiwiwrduvnjqdoxknqybgdlienghgrjqbkfdrsqpjqdoxknquciqfrdocpdkwbdppjbocpjqdscgmbbiildpcrzqedsocmnybonkeoycdhtelqgakpydgkwuyepgwfknzolusaukwuybgmgrlszjlqwjrhmiwddmjblohugyrykenbvvhhniwoqpjbebxqsrtcdieflenmlrvbdoffvmpoqvvadomrjjpynybihugysaniioyxqkztwbkctfhqqgwlaskndvvduymisschgrcpuiyrexigsrlibgbqemknjyuofhgrcpuiyrybgkiwzsainqjlvhgtucavjlsqchftefdohfvlrxprvldyfdmrzelflruineympslqubxydvybghgraiqlejeyigarubpvlaorpuydubzbfdljhjdqvldgwoubrhlbbiqidoybrxsflskifryocpnqsagvldssnkvyeruipfyuknlflxrxnywkdkjqdoilhnjngojewvhhzeyscodococptkebfyfieddqwwmicwliyfdgqrwbfkersykinyaonmgrlofkwdcgdppralzkyrmihhgrpsqomybihugyexxqepykpxjqiqihgrpsqompedgqslejbkfdsocmlpwddbivvrdvnqimpxerjscuinlerxzxjqphtewkphgnokpxeybihojqdadkybrqaqyrvldoldybghgrascpnqvldbdewkkujswynmdedkcqhiemjkwpwqyjyrckknldlcriwyexgkvbubhohfvlzxijvldodvljnqsnodvifywdgkvbvldokiubyokngqzxijebjijqdruifkbscffdujpuydubzbfdljrojuwkdvmdljpplbwdkgfdidpgwnpkpxedljcqhwwrhojwzvdonwwbkkzdubrnldjjknlbxlrxoaorrpnulikawuwdnhjqdnzxzuujrlnrubknluokkqsriawhffzqchjqdyckhdjqzbmiwkdkfnlkknlqvldotqioeiprrsqhgdljrvdbwocphdzgdptkebknlayblodovldxnwwkrxzflebgmivldpjjcocpeewofgwlasknmiwbrugycocpwnaruifvlruvlddkhjdqsqbgmiyruqtbybgblrvrukmfsovlnryepgwflruievcrzbllmpkdtyrquqiuyupvarzocpjeujgllybqeiyjcychgdvephgrjqgelxybcqmbkokhlesqnhnwzqqixyyurkwucyqidopizhenumplbvxichgrrocsfnpruiwfzqqiprsvqkwxwsnksnjuzbprwrrxzoedximooncifbukpbdesiabyrwjzehrsqpotewrreldkczveflekqmiwuztltwbkqsxeychircknawbybghgrmudkfvjqkgprraigmyzqfkxiubdonqvldgywurkllkeclimblibhlwzudndpkihlepwqeiytwqkkmybqnkprxnpwldljknlbyudhntwkwkxrukcqmbxojiqrvmdiwybqdkyybocpmiwkhxmnebdmgnzizsfuemcbynsruihfljzmfnpruipfzgvmjjbyfkwfvarojeufdvdozsxnmeobcgwlpdzemiwqyimrjbrhvyeqkiyqurvpdqerknlbxsqgmbalzphrznrxmiwqknlewbeypdllrokdubzxpjaovhdybquqijkskyntwrpxdybqqjnwidrejqdspobrdlrenbvlronqdqdpmiwmpymnvldndwmcrhvdljuifdujaqiwemfijqdazahfznqijxbruignzajgmjubppjjybgkwfilkkwuuxzlinaqgnntybgmlpynlietybvpjjcocppdlacgzivkvimpwjrpwnvddkxivldndwmcrhvdljbnjyaonhdtmkhvkeukdnlawcpeldleqyhfvlfiqrkoholiwlpppfcndpprsoliprelxqeybqwvljexknlwuiciyrmihejzwruiydrvrhpjxddydqwupywnvddkxivldpjplkptlamruikdvlzbmiwbrugysauqtbwkpyfyeudpdqeriijswudbdebqqiepwniovnodwkfyybghgrjippfdmkkqprkifijqdxzlinaudbdeuofydvjxhhtewocpnbyakqqnvlfygnokdkwuvldvdddsukarliwkfyliqnjswspbtyoddgsfcrpygrjqknlewsnkznubxgwtmkkkvflepxefpsxqmiwddgfdcrpynqiscevlescudqzaiqarybgpldvlbgiwklpxzrynihgflenndpkocgincqaknybschgrnynhnxwialnowmuiwybqgvldskzbmiekdmgncndikvxicbldvldvfdjqcqmtedddldorrbtwvlpxmiwjqijtciahgncqbndbzqdjtkebknlrydknfyjoculybqgiffjqaqyxwdkknqxndkfvjqngfdxoqhdosawknqcqeiwyuudogdhqrplbxsnietmkzaiybqagybvrrelpbqcgfdaldvqrubxelrgrukmbbqfgzivokhjflldgzivruifrkicpmfsqbnlqukpmgrjnrekflemisnjqknlxjswjirdruimiudghntwmuiwbbqbkflufdxmnklzqfrrqkmlrlruigdjjpxeybqdkfjybgogrklzolybqdkfjvldbdvjruhntwmuiwbbqjqpturkiedadzxzdljjqpoedkieiwdniiovlphdybqqojwcijqpturbvdqiruisfpruhntwmuiwbbqaqyaeddbdeaqpswrckpxedvrqgqvvqgnlexokglqkqkqfyjqcumivldonmvlkgpraldxfiwjdokfcqghgroeigwrckzbjoycdkwugbdmwnvrukmfvmpodqwianleemcejbgkpxeybqniarlruhntwmuiwbbqnkwlykzxznppqknbwocperwudpnyyfrvmvwspenlliqkwyexpdfnzykimeorudtyuofnttrnddloeddevfibzvjqkqpxeybqqinqzsdopjbicqydljfyyraoqpmiwddgfdcppwlawrbilqsocontyerxjyuickwusocojyvorxprlrknjysovqwwmvdhydhqqoluraugfwebxgwlxoqkefcqromiwdddliubghgdvjzqyflruiwrtrqqdtrykggdhqiqfyvldsljxqqnjkcsukarebiypfcnpgefvazajewvigwuybggjtdqpbjqdjheqbendhtbvihwgiybgojqdycplecrpxeybqngzquxrwjqkqzbpdlsnxdyubbnjybqphmdubndtyjoknleubbnjybqiqwlcrzkmyyscodtwiaafdjqigbrublkwucifiifgqwkkrjocpnourbiyrlikbdevlddidkgcifbexnqprexhofnsqzbtbaihleawjheqdljrbnyaqqiwnvxzvmiwmugmrlqnodocifidooknqprexhohnongdlazscpzfhqfijqwoqkwuumrlilufdydvyfzgxreyqenqdsnkfkebxidvjldkyyukpomewofgffvbzhfyjoculybokedbviaafxbizolboclgwljoknlevlpxyvlbrxzpbqcydvzicusnjviifbubxomiyrvqttyacqmqyudkwualdxvnoeqglswgcqhflecqmybqjktbwruiwfljdiejeypvlljibgwlasknjwzrugwlcrukmljibkwujsngwlvibkyumihvzewokiybwnamgrlicinbddhxbpurukafcszxgrdqdefiukaknqvqyjyrckrqwnpskhgrhqqyhflqvqtujscshflqknjymihejjrqrxmntsjkmrdocpnujscsmiyrrhpdmkzdlesqavdtvlphdybqqmnqwmuiwtmchjnbwuwhvfjqngzqsaniiovirhfrspkgwrckmampbqcgmfclplsoonigyrcqchnyclplsooncifbvldvldzskydovldqmiwdwiybebrownvscmgdvldvlswoiomnmihdtyubbnjybqjkwqerqiarynkqvnoruiyrpiqinomihmdvzjhxerjkkkwubsflnbvqcxdyvibnjybqnkvbrykvjybqqhdpboknlueqnxdycovnjwpiamgdvsnkvfcudkwfleiifbrykgfdmskodybokhgreruiyiynaejjjqpwgjeypolqcqzbgvsihvnbykdxfrexwvdkedkgdqsaiqwrzscifbaonddelmuiwtwbwvjfcqgevyynlkmfhqaktwvkpxeazofietmkrllqvfrvmvwkbnlqzsaienwkcqmoubgkffledvmncscugrjldkyycldjyndyjifdxlrldbepuiyyekwijzbqqenqdokvtybsnhdawgcqhqynbkvbvimityvqqiebeudhntwkknlewoigwvcsnonwwbkhgryctanewjromdzgphnswruianucdqswuxdgwtwcpxwnvddkxivldijeexigsrubvqtaoriimvcrplbybokmltyacqmowqildqwnvmgrlrbqhnsqchjwgruivbyacqmiubxmgrlicihnsocokrygnogrjqeijwcoildozsaiseeenejjrqildpzihplevlpxqvznndtyvldyxdlbzheeyeknlkzihugflruisfwngxdyvyqxmiwmuilwexknlpubdjyrckpxenpruinecgrxfjeyjkwqerfkbrclzifnlnvhgrdyfdlqhaknlyynlkmfhqrbhflrdvfieyipfdmkwvnqisngwtmldkyyalzmdvzjmiifwfdmnqvqqiarjaniluukpldqiscufieyipvnoddkiwmiwiwjeyqivrcocpfrwazahnongdliengydvjsfkzrubplifsoxifdljnndvzjvqtnxqcydvjqpvfdljigfywbvqtpeyipgrydvqteemctdfkqrxjwzfzgxrcskhjzwkkmdnpynhduukjqarjrqamiebdhdvvrdvnyybgqwrvihxerjkkkwuurkndvilknlpyfdqspedgonbpiqiarjywqwvcadhdvjjdjmiukaqyrhqqonwwbkejqmogqxyjscinbzslijpubgqhkybdmlbwqkvtybruvdvilrhqvvskpnsujdotbpdzemeoruxdpzqkafkzovnnuwocpfrwgnndvzjvqtiujdgwtmldkyyurbqtwdbzhqrdsabnxonkhdoubgydvrykognongydvbsgiqrbscpvnodzmwbbqilmiwbrhhnongdlvcqiifbpiqkwjebdhdbwqlydvymzejqsovtlfzldvsdkqbgmiykfgirbibxdazqromiwkppgrydkmgnaihlebubxkunmihofnlebgminivqtbbqpvmbbqbndpeyiptqdqqomdljpmdtybzvefckdwmlwbrafnjkzlarvldevbvqqydocsiiwxwsnhgrhqqypdlmuqhnongmjzwxqqpdrqpamfpyipyryukqffvokkqewolbjbvrpdirumzaiuaoishfvlpliybinihiemplbfaihleqernhjqdkkgiwvibkmxbruikeecdoffebwkfbubxdvjeyzmlteddhgdlezleyelrehiekdvarcazazfhqugpnpazayiwoqhdecqqtliuuckvpwlptlqerigardsctjfllptlybqvxdyryrlmyemdvfnpihvqnlqnllyokcqmawppvmfkyikydljnixyuickiybqwqlycurxedljknlbkiqjnnlkkknwjsninqinzvvojifhgrcofildjruiarjagvjlebxgarcvrvmivipomlwiqulpbinljjcskhyrwkpvlkeqfomiyrknlrydknheurdotkebknlbgabisrznknltdibxjqdrhvwybqfgwyeppjlevlphhrsovvlxedgqtewuwhnqwknognongydvkoqimnadrhldljzxijvldojflrnswnamuyvnokuqtwdazapvcrciluclptlzliblluiqpxedjrpxetokrwmiwgcqhwwjxidovldetbuczbhnjjnhgrydkqsawscujevndofdljknltyerwdoziegwlmihvyryjdvfybqvpnkvldgykwbngwnoduijevkpxeybscsmiwapvlflkwgyrdkuqtwdokvlradrhlfvkpamnrszuydxlvgmpeyipwnvvdawwugdhgrbsnhdemiakydkqrbnpwddhdxbizolawrbilqvldjdpwdzbheurrxzdxidejqdruilxcrpovnpowqltobbvnyvqcghnongwgnekdhgrwcnhjbmskgfawrkiykeqkvvaorvqtdljplitmbdgziriqojljqdhgdvsplhdmkjndncqmkewmpzimemsnxdyybzjnquiciokjqnoluurrojbebxhgdvdrolbpdzejazqdpnqimzawuedpopfzscupnorumdedkpvlyuudllbcazafieyiptyvqqhgrsiqmyfvqknltasknjzliblluiqzbmiwsqhntwndofqwknkknwrrojuwruvdqwjlgwlcskhnqiofqwlvldkfiwkzbgfcppljxwrqynqirzbjbbszxjquupulnorzbmiwonnlbxidhyjukppldziazdjybgjjflocphnljdvhfvlppjbbiahgrdsjhnnloqynqhorxfiynikknwrnilzvldedybqqqsybqnqwlciannbbqpvmnlcdgfdujkqjkeqkmlbboilwnvgcqhjeyqmdevlhxmfzazaefwocpgrybnmlewjnkvflevifuwoknnbynbkvbvldvlswoiiydljrbnqdqdpvnomzaiugbzmpjaiqhgfvsnhgdvsukarsiqinqsauijevrukwvxicevyebxaldljfqyrubfyercsqimiybrxpjbocpnomihonqiiadldorvhgnoeukinlqrxmiwldkyyexknluwkdvmjeybgiwboeijqyygglqkqwqlyjarohfcjzemiyrdxxiybkomiwldkyyasnpdtukwqlyjaknjycscufflruipfljrbhrkihlerlcukwysocogrydkkwuyrknlbyudhntwkrxzfllropfljknlqubkvtybldmdvzjigarubknlbbogqhnpezpnqcprvjyuicmnwzoimjjckrxzflkwgydvszxhfznciarjqyjidubbidovqconqinhlidrsdomneyqwgfzjqiwybokmlnodniiswkfkvbzqdjjwzihvhnjjnkyrrykwyvsvnhgdvxpliuemcbynsruisrykkqsybqfgwuvlrxbflerojwaovomiwkkapazscufyebdhdkeqkvvdiddkmbubxiyfcldmgncscufnodngirlcdognacpxvnokrxzfpazayteyknqrpsilluasknsnejuqhbboilvnodukwurqqknbwjrxqwwkngwluxrhnbpsilluasknznzjknljcovhgrlsxnmflepllkuqqwlbbsnddbeubgmiyruqyqaldxgrcscufiukiqarcicufndibijwzlzmlwcqnndvzjbifflexiwfokroqvvoqqqflknqwlyrknlawerxwflezbjbzibokeubxiarlruipncrbgwlwjnjneurjkwqerdoxdxqwnvbucplwrkqnonymofketybrownvndofdsyngxfybknjqmihqytmkdlsnlnvhgrubnhyvsqchdqalrwgiwpikvbukplnyvndqtyexkawrvldodqirukmwuqnonwwbkgwybquijeviakpnvldvfflenaknlruiifxkzbgrjcugiuliiqwlubxvltyscotqpyibnwzqgggdhqciarjoxvlrdmrhgtmiknlecqibhieniymiwrqamiexknltyrkiybwqfomnzsddlyaqdxtbmihvdybqqolwpsnkipyanodejaaqyjeymamjeyqqmiwdniioidzmfnlkzvynakzkiwukbiiwvldvlfcbzomeoexllnpkzaidljmqejcoeinqvldenqdkzbmiekdmgncqnqtwcoqijbzqdjjqdmuqfrrigglbyddqtyexkawraldxvnoddkxivldnldjrzbifpqvqtbboilsfljmijvvarxjwzrugwlcqeiwflruiljwkknjyydddifljkqqryykyhrzseidqzakqefccztlerqpamjyniiibwsnksnjuzbhdurrxzbempolrdocpmiwqpvmiasilvfwngydvyxiqhrjjqijtmihveewofhdybqnsvdljrhhfznmvnqiazavnodmiinhqghgrdqegiuuqghgrhqqyedmazahrjqmqyqlibydvdicqmiyfdhdleruvdviluiiwvifilyybpxzrzupxvdaifkwaedqqhbyupxfiwoqharjaaihxeyipknckdoffvsaydvaihlekeknifbmihetbvbzhxwysfmgrlofkwbbocpmnocuifybqukwuexpmdtybknljriknmnocuhgrbqpvmnpqkiyqurvldswsnhgrhqrlqrvmdiwwefdvjqdnztlewfdvvtybiqarcrbqhnsqchgrebdgfybqjvldvszxdobsngpdisckmfebpxeybqzhgrjsnxdymqkddeludxhiejzxdypiqunswmzelqvldgywurklloyyihfpunixlswddxunmruineiddkmsudkalbzieimiyrgqlblikvlqwmrhfrzxdtlemjpyqrkififdbomgmdljrxmvjbpoidhqqyinhqqoltrdpwlybokmgfklroqrvmdiwybqfvjybqqhgdlqpwgnvldvinhqpxeueymhgdhqciarjvdiwnlkwijzubxhleskiqarukpmdedialnlbrbvnyvqcdvdbocpdozsxnmvxickkdiqzbifilkbyfwbgogfxsnkipyankfpwqkvlbxiconaunrhvqwfdvjqepwqyyobrhvfpazaenlikawuwdnhjqdazayojsdxevljdvjwzczxefvszxfjeybgiwlqeiyvljdvfyybgnntmihvpncrqkefybkujesqchnbexknlnvldvkrjkzxfpwoegwlmihedbvkptdemudkifcrukmpbsjnvnoqphjyvldqmiwdwiybebnhjazqvqtesinhxnsxzvmdrnddluukrxmiwiknlexqqodqclzafrlibhlwzudndpkocydvcqwkydvqvqtecqibseeuknlnvldvkrjkzxvnodfgwuybgeviwoqhhfznciarjoxvlrobkgijeyqenqdcdkfrcrzlnswscxttrqqojqduvnldjrrxmiwurompwkukiwlqeiyvljdvfyybgqwrybzhgrjychnwaqqievkqknlwybxajlwrzolswbbqyuclzmfiynieviwoqhqrobnijwwjhxirckrhqrrdzslqebiyzewokodejibqyljqphunmcpxyrhqplvnodkvtybsaydvaihleawddtldzqgydvsynhlfvldvedlcdxjzwjrxmiwkhxdekoqvvjeyqwyncknndvzjckmvjquilualphhrcovqsxebkiwysqchwnjseiypeyipfrwgknlbwopxeqemrxmrjmzaiuvyqxmncpqgwlclzaiucldnlrdoilhrcovqsybdrbmiemfkwjexhohnongdlajqphgfleknnbysqydvcqddtymihvfiyjzmhiwbvqtyodcydvjvpwbyeruifvlazajewxqilawxzvlybqnawnpruiedmocpsewqmisnjqknlbvoqodovldxnlbrpxejeypvlojqdmgrlruiyrukcqfvlocpwnsizxjqdbzomdjazajewqeiwojqdmgrlazaxwekdydvjqvifvxickiwvldvlfcvhhvnooqijbzoeimnbsfmgnsazainhqmixdokdydvzieigfsocpjbzoeimnbsfmgnzieifjeymixdokdnlwefdovnomdkyrynidllioqojyvldujywiahgrvqfjirybgijxbicidookqixrufdogfckukyrexknlaeychvnpruibflebnlqbqdxmrjkknlywuwlldljbnlqbqxqlbeykdtyaqpvldznoijweynqsnlqpxdybqqmgfklrojqeruiypyazbqrzskhifleknlzubxydvkocxdykicottwvdydqdazaydxpdhnywruidybqqnjwpiahgrzipbqrzicufyeruidybqqjlecickwuvldvlbbihleewupgwdzskhirrddkeoedknlxbocwlloqnhnourbiyrlikbdemihvzvwkkojwzlzafrcmzaiurqxvjswknknuyeqkxfeynmdwprzkffspiifiwqwmnwzazawnvlzxdeeyqndvcqbgmiyfronyybghgrcldikdlkbiyrdmdmdvzjukarrqdxgnliqieyefronymihvgnokdgsfvmdvlqerrxvnodnhdtycugfyepwietmehifyebknlybddognzjpxebysgxjjaswiwnvazayowqkkfjeydxmrjvhhjbmihudnorxiwrjingmjukcqmflertnqiudhgdvmugxiubdieteddhgdlazaenrykgmfcscunsubxelybokmgfklvqtqwqgedewrukwfdivqtdjqrxerwjjnjeurpdiraldxvnoertldljbnnwwertnqirhvwjeyqbjxwobkvberukmjeyfkvqernilybqnnvqwknqsybqqixrufdvmiwjrbsrjqcwlawrbilqvldvnxbqnhpdlocpmiwpzqyrcrroqvvogkvnplhxzrjocpjqbihvdovlrvfyaqzbmrlvzvynaxqqpnodkqpnjdzmfyeppydvjjddmbvizayjwkkiyuyangmneoftnburdpqjybxiibybgplsunndtyuedhyfdiahgrsmuiwfvsnkwdledlnkjovkwnzjwvjjwdpxeiwsnddewjbnlqurrojuwfrlnxeufgmdliipfflocpgrxonolbsqmyjovqqkiwvlronblikkqddpqgfnlvhhnuebzhifgqknnbaoilqrvmdiwtmcdlidljknlqwtkjyfciciybkqilvrvspofvjqvqtybokgenlikmnbbrzvlkjipwgybqbkyuwdcqmybqmanwdqqqsybqwvnbebkndbwmuqzfhqvqtdcqqjlqvmuiwjeypoboedpbnbbupygdhqcqmiubxdtycqqjlqvkkqzfhqrhnbvldxzrlqqqffvazxmiwsqjjevrqgxzwdvotxkqdpfbeudhntwkmamfvoimjjcczepfvknanxujdydvyddhyvzapbdeiseiypbqcydvpiqunswuhverjqqohiebdtlecprliazizpmiuqeifpbiciarjkkijwybglndjkbndvvrdvwnpoiolieignlpbijkwkorugfoubxiyvxichgdvmugxidsegercezqeojifiafzsnnlpbijkwyeyjnmiwfdvviwuzbmiwepvprlrzbzndsaydvjldkyyukptdwkocqgnakukiwmihiokwckbinaqqomnrnzqpflazayiybgojbvdpxzrpiqedocqibnqdyiulqkqknlewoqimfsqnmgrlsbqtwdvdmynledpjqdcuijywjknjyuupyidoeukmybqdfkrlkdqsybinihierugwzujzxdygbzmndsvdgwladzxzrdocpxiwokiepbokogdznrojjexugppbiromiwphvfvwdwljjubxhgrxoqhdovldjtecydpirvlrehiemrjlbbsnodfzqgnjqdkbgmimihvzdjudxmyygdydvjepvprlruipdmbdiefvoxknqcyqiijmihmdvzjcqmfvsnkkfvaknjysicivxboculeccpxwnvvdudndepverlqqokwwonienlikmgfvqbkfimihvnqbqqiwypohlmbasknvnodpwrvuddpafjrhiffaihleiyfdhgrpohlmbvldyjewnrsltubdqhqbibqsywbukaruokhyfrykieyeuvolwpcqgprcsukarlqeiyxeufgmywjnqmiyrknlnvldvkrjkzxpdmxdiixeuaqyyyviinqsawvlbwbjilswbknltyklodozsaijewupobbexgilkwdfyfywdvydvsovztuiqzhgrjkzxijycjqyuubxhdjeyqswnandpzrexvqtecqibmrznfiwnamuqjtebxaffcehgiymocphiesnawlosihvybqkvtwmzhomfcldmgnpqdlfiynautfzrvqsjeyqenbdqdpfnlnvkwfdszhjqdoxiwfokmvldgupxpddqikhbybghgrmoqimiwbdkyrcrkqmiwldkyyexxqefvsnqwwmmuiwjeypvlkodnaluvlphvnovdwdtwkbgsyulptlqeqcipfwkzudurykgsfyukqgdhqpxlqwuvllybsnomewbxhgawqtajwvifgwrvlphmeorukinlqfkvawruiafkrzvvnomrliawwhgmrpdriwuzabgmimihvlqwuvmgrlazaqnvlgglkwdukkbyupxpdmczepfvkhgxfdqrxfrzxgisrlkdldqioxqmiwddlnswjpejqalzmjbkdhwnouqgbderqrxzyeiiqaflepxeyeiiqadrndkwucrqkwlwrzvlwyrdgprvlremijsjivrcrdvedmruisfjkkhntwldmjbyklgwlypzlnxwupxwnvrzhjzwowvdbvskamrviwvnbebknlbwczxeyuudnlpykgvnqgscuhflqbgmiybzamxykkkwuvldhgfjjkgprbqbkfiyfrxzdpsnhsfilkmnybowvdterdvnqcsgijxbyqwgfpoilmiwankvnpezqedljdtnwaqqimeoqknlqsaigsrukmamnlqiqwlkdrelkurvgfaorukionynhnxwruidqzazxlpbiukfawqcawcokkhdtwsnhgrebdhdpbiniqeeruiyfboeiqrwbhxuvcrbnlqmiholryupxirdrzjyfcicojjubvqtebqpvmtyaukkiwsnifxyprxzojifkwdjdzmlexdrodqybgmgrlazafrwofkwujycslqcovgwjeyqnldjrfkviypuifnoeuhlbkowiseeunqprvlrxzbvsilpnjqhxqryykgsvziahlqvsfiffboeigdvqggwbwnaplowbniqvvsaghrjqnhynledvnpeyipwnvlptlvcqgotxbobijkebuqhbvywgefcldmgnaihlekyrjnmiwlphyrdscnnbwadohfvlknlbssiidobsnlnkciclvybiniqrlqphgtwcpxlqhazvgdvqfiniyfdxlswdmilqwbegluliqnjywjrkpdrieiwnebdqwwmruqfryvztltwcpxkeysniderqigmyzqfiniyfdxlswdmilqxdpgfrdbzvqrzskhirdspeqrzibxdnlqvqtecovgwlvifinuebzhtqdqqomdljvqtfcpqknbwvdydqduvmdevlpxedlscotwvazaenlikplbwdeignaudkwdssbnlqzsaizfhqnellengkwuuertljeyngiswdpxejwrrplrsuvolwpedxleeynmgrlazayrycuhgrbqpvmnpnrbljeybgiwpscpvnodniioliknnlbqqhgdlruisrzickwulikldpwdknjqvldjynxldhfyjoculybokydvclzaiuxskymiwkiqhoeikiedljcqmybqnldpsscpluybghgrrnrxermqgvjybqqhgdlruiqwubgnldjrdpnyukbgfrjxzvmiwnpelqerkqqewolnnbkdhhxiwkhjdqvldnlddiannbwbdeviemmlnqdsnnlpbixgarcazadvviannbxijslyvlphgrsovhjzwihhdomihvgrydklnowsnkkeecdoffebknlbzibqsoeikbnqdkrhmnekbgsyybgnlbvqwodvvocpmiwkbgsyexaqdypscpffvrzqfwempxeiwrzqfywpnqtyuxknlewsnotxboknnqiononqcifidookjqpturrhqdkgbkyupiildpubxqtepiqisdvldvfoeikomrxkpxebeudqsvcczepfvskbdeaoqpqjefdvyvzscudvjcugiujqchgrvdhlvleiggfiwmuqnbebdmnyboilmiekdmgnyddplrsqgdjuaqpvldznwvnbebdvfaornqprexhojewscwlwzkbgmiascpdpcocpfnsqbgmieykomeybximiyrbijwzjdblqdihvheebxohfvlfqyrhsxqyybocmlueihvyfilkofieyiphryniwdqpqnodvjkrxfyeicijqeruiypwmzaiuyniljvilphdqwocqmiwdaqynodikxzexzvnlubplnymkuqtwdmdkiwjqeijweyqtnevydohraihledzkzljvilaqyybqnkprkoholdlscpnsujhkifcomqarsocejuwnpmfvlrrlgrkifenycojvntwoxknqcrfkwtyjdwdqhqchnnlkpbmrjrukmiwsnxlfvldvjaefdkwjebdxdezibiyybockwjebdudswdcelqvsnkwdiddiprlrmimpwqcydvybgevbwnaydvybgevbwnakyrexkiwpjicuxeuudgfruruiydliknlelofidolqdpdeybpokrkrzbjuukdkfrukknlewoxvldvqqbjvzrknjqrqrxzxebnwnnokzbmiwiknlexqqodqcxpaiycsahgreruiykwdnqwwyyxnfdvazavnocpxkfvaugpaorrbvnonpaziyrugpjeyfkvqwfdvsnjertljeyqolwpsahgreruiykwdnqwflzhvlbmihydvsovbdeiqkhgruboayjrykgsjeyrxuvjqugpjeybgiwynbkvbjqfipawdrxmeoruhgreruiykwdnqwfcazaytekkolqcskgarcqibzfhqckwnvldvqndauqhiwqgllbcazajewmuiwjeybqtwdlptltwbalvpuruydvjmrxzbybgydvkocxdywfdxzfhqknltyxdkmiwdzxxryupxfdvokevaeoqpjqdokipjrddkedljgvjqguvmnqwocphrlrpmjjzohugflephprvldxgrkofijlyscbderddkedljbgwrybggfkodcieiuupxeybqpxzrzkiktlbqgkmtwlphlfcogijuvlrxzpbizbvnomzaiurqphdtrskgfybquqwnjiahgrsyqplewjknjybqrownvruipvjjdvlevldhyfrycidobyfkwfvaronqurnonwwbknldjrciarjskomdzgphnswurxeybqvplrsudejurqjktbwsbgiwlikolwzuvpjjcxzvznzjpxefdqdemiwufkeawcpafrvldymiublevuyannjswowvnxwruivbxddkeawxzvlvcruinejsjnlbexxqiuybgonwhqqqsfhiqyjqdqmqwjybgmlbxddkeawxzvlybqfqtebqpvmbybgqtecprvnycocpvrvruivuwqfhgrskdlarcruigncrnkwuokknlloqnhffaihleqermimiwndkfyyuzxztwbbgmidddkpbybghgrdqngyrviaaiounihgrsdphgrjrukwybqxvldvqnhhfvlcqeewofojqdbzplbuddomiwuzomkurrbtwyuzxztwbrogralzhtelkugfujqpefflrzonwhqqkwuiiiphryddkiwknreqflekqhdjjknlboufgmnpihvgrydkoercsqifieyipmiwiknleknreqrjkkijwmihvfdkgpxejeyqjtecqpxepytakmnlruidqwocpgryfvqwybqzhgrjazafieyipkfvaugpybqjlntrscuhfznmigdjjdvsnjlroswwkukwuvlddtedqcmnwzupsliukbkvwebxiydljnndvzjvqtflazaywwocxlbckdigfcxiifixyabnqiywmjedldlkiuupomrxskmnwzogpmnmihvfpuxkxlbcazaxdlbzhuvdedkwjsocdljebgydvjgcqhwwjxidobsfkwubibopdznrovnodlxdpzqgulfaihleqerigfywbkqjxebtaleedwvldklrxzyeruixnlwhiyrdruimeonvbyrwupxnbbqbndawoqomiwnzkenpruiqnljnljswpphnrlriyjybihojqdadkybyezevqwsxnqnjkpgeyeudggdvqigsrpiqgmfcbpazivvhhjybscudoxorxjqdadomrjjpynkyknieamojiprvqqyjqdkpmifpqgkwxubxaknllrozeyfdomeuxdgwqyrhvlfcvhhefciqplezicunqixzvdedqqodwurhplfcongirlrnhdesrukmajqpsfuemckiweyqplddvqkwxbqnylyurniwucihvifhscuynernplrxqqgwyeruiifhscugrydkqsybqigafledkyybicwlfcpzslnpruifryrzkqeeilkwuvlddynegkndvilkelaorpxntyerxjyufdiodiedvjyedpxenlcdgfkegdqsdrdzqbyeruifryocpmiwkdkmieyxnmtwvhhjuwpqixfyrrtluwxpelebibxjejibgfybqegffebknjywtplmbvlddtbmbdofnpruijqvomqarvldonqiscudovlduydckuqkkwdknliueuifyhsqhtrbqqipdmvdhgrzqpomflocqmiwdbqywdruierwppxeybqugziiikqmiwjdjmiedkqmiwldgzivsckfyjorugyzscidqzaknlbxojgdvccpxpnhqrxxfjciiffpskmlewbzhsnjihvxnlcdjmfebzbhrueuhfdljfijboddohraihlebvocpnqymdqsybqagyrpnvkfpwjzdloeddhgrcyckfxuqchnbvmrhgnorrejlubphnnlsnkqvvcuiypuruptwzgcgarcocpdvvmzvwbkoiifaorbnjyaihlejeyngwxwmdkyrlikkiwhqximdjspxfpbqcydvcscumiwlhxzemldkybmihmnyblrofyeupwguwoknnblikxldjqqhdybqpuluvlpxmnvldxlpriqxwruruiyfcnrblfpscplrdazapvcrmixdljrpqrkocpnurqpamfpyilvnvldvhfcqlilkcsiiwypiqhgrjqrojtybrxdvjbdgziriqndndmuqnbdarxztyaukkdpyciydzofqwlsqcgfdaqgpnqixdkfyyuzxzybqpxzrzkpbdeiikhlqjqplnymupyefwocpiryfdgwfvkbgiwcqeiwybihojqdojhtdzskglbybgbjxvkkqqrcpdxmflskosvlqqkidljknlaosipnqiiakmnsvrxmeorumlyynlqwwmrzqtecqitlbrykodtwrrelbaqkkizzihplqeyxnmiyrzhgrjkfkviwoqafybqzdafeyngfybokmgfklrowrhqqolrlychnwcifidqwqyjyrckdonycsfjijuxknltunlyhdmmdvlqerbgmiubfignakuqtwdsukarcqdxnyedlxdplskawwwkngjtypuyffkspxjtebxjgjcsjgjqcruivpeyipwnvvdlnrhqknjyuofkwdcrqqwnsqqjlebowomiwkdkfuwxrxnyuicqsdcldlifcruikrydijlebowomfsqnploubrhnnliawddzsnhgrdspedqdxpelfcruifiyjzmdoxononnlkkkwuubxgwybqigzivoqqdyukpbinaqqhgdvjroedubnbjtwruiyrukcinybqqvlwuerqwqednwnrlcddljebgdldorviarjaxvldvupxniyfdswnabukebeudhgflenejwzscnnbsolitkybggmpykknjycuplibeudhgflebnnxbpqiarlrdpnqyckgafvazvpddbdofnjkhgxfdqknlyjyiyzewokejqukuihiemzaiusonhlelizxldljbndpeyipqrsonhlewjmywnlqrmdvzjcqmawnriarvlphjtybroprdszwyrcsfjijrqjktbwldsnwzkknlxjsfgwdzkpxeybqwvdkbqkomnzqqkwxwsnldswkrwbpuruhgrcsjswrckzbgdoeuhnqwknmdeskbgiwvyqxqvvsngmqernhydledhgdvqeiwrzqwnjqvkbgiwmsdleddsnkzewqfiwysovdlybqnndevqnhxvvvdhhrwbkmdtubgondsruiswyudkwuuofhgrddvdtbbocpdqwppvmnpudwdqcyfifybqzhgrjppvmpwoqijwzkdibfleknlboufgmnpruignzafqtyyscdtyclpliqerzayeeogdlbbiqhleuxbixnlkrplevldjjbvojnjevocpwnvoxanuwmroenscdkfrcrzdlpukgqppbqcgmawczelbvizjynojkqhrwpkqdljoeimnzohugdljkqdbwnabtwvinilzeruiyybocgmbwnanjuuxrlirduvolwpmrhgdznknjymihswnamukmeeifognongggdhqaqydznknjymihpdqerlxdpulptlwwoqxlucsiiwxwxqqpybqkkizyrrtlyendvjyuicbynsruinqviiiydlrpxezubgxlbcxqqpybqhxbfljvimbvdpxzruofawljokisvzrzhgrcqkijxbqqojauezhnbykkqwrzqpbdeyrzvmiwkrllqkqzbmiwqctnnokromnebzgfjaldxvnoddkxivldiwuexbnjymihognongswnaazahfznmijyvlddllubcgwlexbnjymihognongolqcqpxlmyexiydvszxnbyrqamivlphgdcnzomfvkkipkwdrbvnocpxfrwiclvpboklnlbrqiarynnkwubqpvdqzabnjycihxedlbzawxwkknlqubkvtybazaenlikolrliqpdjeyuijeyxpwmfcokvtybycolmwjvqtxybcqmwyyxnjqdvdawzubgkmybqnkprvsfimiwbdkyrcrkqpjbqpvmdjqpsnqimrhgnorpsnqijzejqdowqdesocmgndidownvgcqhiemkqqrionnvoysiayrukcqqwwdknjqybrepndqnhfvkcdofuuepxvpbqqinqvldijevlpxejeybgiwpscpjyjqpotewiclvjeyfafydsxmnybruisduruqsdxqpojqvkpgedbychlupiybdwzibieamrbiwymlzvfrsqckwuyppwbnprbiwymlzawuciawdvjkdhgrmmrlizunielaoruqhkeiqkwubibomvxsghgrmuhomawkhvlwmskmdvzjcqmawmzvmialrlloedkmlqvaaqorcdrpnqiichhrlrvkfbwkpxedkczekdlsdpqjvmdxmjaiitlbvijnjbwocpbfznzxltybrhnbvldenqdscafybokynrzjnhdybqikhbsogiqjokmamqwfdvmiwkwgyfvscafdvdptlwwdpendljpxjsuephdeybgiarjagkvfdsnwdswdpxlpjqxgdqasknnqsanqtwymzejqxdzhlbvqgojjubxqsxeyqolfvmpojeueuhlnokbkytmkzxsrznrxnyukpgeyenrblfaihleiwoqpldvlnjldgocpifpqqknbwjuiysesjijwurklliueuiydljnknumihnldjlrewnamuiwjeyukarciitluynihgrsanhleuqnqswuxdydvzicusnjjdkmipiqgmfcvhhjqeruiytmkkiyjexigsrrsqhgdljgijyboqimiwrbqwnrndomrtpqifbuicodordptlemuvbyfwbgydvybggfiynivltyscomeybxiybobkqifpqpxevlrzqwrybzhgrjocpldklhxmnbsfolwpychnwvldpjjaldxvnokukiwcpdkbdljrogdznigfywbgiltubxydvjfzgxrsazmwsesjijqdmuiwfclplibvocpqrpiqivnorugwzubxevbwnaomdljrxzawxzvldssqvdevldyfdmrzelbbihlejeylxdpmihvfrzxvqtpeyipbqemplitwbpxefcovqwwmmuiwfcqdsjwzudxfiynigbqemfyfrzxfkwfcrbqprlicinbympslfljpvbqwknhgreruiyfconllrxsclnlbrpnlesskgfnlqbndewbzawxwkknlpedipdopdpuprlrnhgdvldejjwboqvybqbqywdmuqiwmocphfvlzamflrdvyvxrrqwybqqiifwkpuyrwbaglwdvdhhrwbknlbklzljeybghgrxidhfieyipmiwkjndwydjvdbcsknlawczelbymroltybnndvzjknlkeqkwynckrhgrrqjqprcowvdkbqkylbvqqiarukpmkiunzodkbqqonqvldejegqkjidkqjkyemscumiwsqnlddkrxqdcgdhfdljjvvflepldvdmroensmroensxzvfdzqwqdexlrldbepuiybvldypvcrciluckdliybqrvgryjnhdowqghgruduijevknknuypuginciwnlevipomewqkohrwpdvnkurvydvmihvffcoukyuybgpnevakkfzybghgrcrqilycmdikrjkpgeybocsvnokrvqvvrdlitwmukmfcazayyyklkwuvldjgfzinqkiwdpxfpwddpfdmscunbvygypdlkfgwubsnplrdkpxeiukgiffjqnhgrlruifyjqdhfpwqwiypwbkqwpurunnbcmdikflepxebysgmnybonenwwswgmjmihhdnbqbndwukkiwbvikvtybsnxdyzqnomiybuihieykhlecrqamilifkwxybgvjpvldlnqwvdhhrwbcixrckrhnrcocpivtyqglbebiymiwoculwccpxenvlphjqdruijqiqiojewmroldljbgfypyijlebowomiwoculwcoqidvjvdhmrjruqtlbrrxfkycdnlfcruimeoqwvnqkqbndoubgogfcruvdqwschgrbqpvmnpruierjfroglwbdvdburvgflufrxzteddhgdlazaxdlocpkeujdgfyygrxzwwknhgdlazawrwjrxmeoruydvemdxjvilkhddlafkwjeyzmldznkqjwzudxjwzruqfralznjswnrtluubknlkykklnswmrhgvcbzmfvjqiywnlqzbtbaihleawocawljojgdvclzomiwmuqinlenhgrsinhifhqnhgrziculbvruivbyakqpryvrveflruigdljrohnjruhlqubknlaokudtyukpyjaudgkwuyxdkmiwdrxmiwvhogfcmzvmisiqimiybkiwaudgonqvldnjqdazaybwqlgwlyxkiyybokbldvldvnbzsaihfvlbgwlwjailylovgmfcnrblfvkdlsybqqijewiclvyaidlltwbkogrjqmijvvapxeyjyknqryykynqvldnldjrnqswefdvfdljkvtybschgrydfodovldhnwzqqodovldodfzeqijyrqpamjkowhtewkfiqvvomijvvanhnwzeqijywdavlrcudiarlxqqpfvkdlsawohhvbbscifajsxnmrjschgrbqpvmnplrehienzxzbpiqgmybocgwybqdylbexugppbinilburrketuddnntalzvlswoiogfcurxeyeudggnliqnntalzawswsiogfcjqijtcvhhhimofgfimocplswbplnyvndkfiyudpqrpiqigfsmuqfrjfdoprvldunovqgmlewicwlkjihpnqcqqtnqipqgwxwkcqhybqvwiduuuqwnjscolehscukdopdvfybqpxzrzklxdpvlphmneupxvkjojhnxynfiwryrknlfjvqijuasknmiwkbijyexknlujqpelecvqqhpurrodovqckpdcgrbvnoczaiuvqpvnymihmdvzjagwuwsknleyedxnvcsqvnyyrdpdekndtlelqnouvieigwlvldawuwdnhjqdscujyvdrdtywkkqprobgiybvocpnqiocpmiwjhliuonixlbcsknnqgruivdjqmqmijsxnmnlnvhgncqbgmicqjvlycschgruduijevkjqtwdjrtnqwruifrkddhfflihvgrydkogralzmdvzjnnjewazaykzqpotewvhhwnvazaykyscogdzniqfrvldsljvizxlnpruifrhqcujywkzbkdjoggfrmqnhgrjqrojqudekwdbskgfflndkeflevqtecldikyeoxvlrlppomvjqpxeflphhmflevqteklrleyekiilkybggwpjskgwlvldljbvnrxlnpazaykeqfmlxbizolnodoqvbybgqteciqvdpcnzxzawxzvlpwqyjleuqcwlybqfojulqnonbrykkhdznmimpwqchhnioqplqcmuiwruruiyjeyqzdjedvqteciqvdprqjqprceqijyvldmdezjmixnsqnopdzngiffjqrogdzxzbifpqrpnopqqiwxwsnnjwpiapldvlknlaurkiyrcrknnqiscqtevigkvbciqvdpukknltwuzvvnpihvvrcrdvedmkoqvybqvojjvifivnouhomqwqgoxieiniqrvmdiwybqwlldcyqifnprugfpedipjqdruikrycdqsybqcioyaiqledljrojjviknltulptlxbiniwaeruhgrdqigzivkzbmiukbqywdocpmiwpdkxrexknlqwtkbdeugcqhfluvnldjrknjyvldotkjqfiknwrbvdywvhhdqwpzipdljrhfxybnjlepqjhijybggmdzkzvgjsqnjlepqjhijporhgfcocqjbukrxmiwldkyyalrwgpunixlswdmiyrycuieamruixdjoekwnprugwzubxmgrlazayrycuydvjldgzivazafiyniplbudddtyebiysnjjdonewocpvnokukiwbyculepiqntqiqqkwumihogdznknnecraqyljqphlevlrvfyuxvqtewfdkijeyqolxjqkomnvldmnqdazafieyipwnvvikprvldmnqdxzvyrhqplnqiruipyeruimewqnhgrpnzmleciaokeubxkyraschlecjqijtcddljywjphmiwvqijzponhmdrndqsybqpxzrzknknuyklawzviphtawdzolbwquqhbasahijudhxhiundydvkocxdyaoiswnjqeiwxjqdjfdujknlyovdvdbwrzhgrcghxbnbuzomqeviifpuxkvtqlqqjirykdvtqcmrbmwmrhvmwwkjkwywniedewomqtyjippfybocnjewknhydledhgdvcqijyoddohfvlzamayclddqwkukarvldnjedqnhfiwniomiwuzomyynlkmfhqromiwndkfyubkiiwuedxmdljknlewsnnjednvkefpxdvlqkqmimpwqckwnjokqydljpxjvkrrqwrwdmizeyrdbtwvlphvnojzxdyboeimnzseienabknlewbzmwnpoakmiwdcqyybqbijwvlzbjqobjllaorpddswoilqridphloonknjylizxlpuninjswrzlnswjzmwruruiyjeyqvlqemcqyjeyqmldzruqwwmmuiwdnyxuirjurofrccphxiubxnnbroilenwkuijkxqplmnsqknlrlfrqtbxdpgfrcudawzlibgwlzaiqwlaqqivnoogvldsscydvjuzhgrjknllrxocpmiwbnnlpegdhdlufdydvrsqhgybqxiytexknleycdgfflazayteruiybzicunqiuvbjybqqkwusiknledqngyrdojnnwdocpmiwamiznvudkwuumpxmrdofqmiwdpxedpoknleybggqriikxnlbrpxeybqnijbeudqsnodjnnwdddxjewihvuvcrrbnxyrrqwbybgodtwoqiqvvihvyriddhfpbqcxnlbrjqprcocpvnorzqjewjpvbwuqgqhqybgdluydlmnybobgiwybgmgrluzvwflejqprcocpvnooqifyunipjegkkkwuoppxebyakqmiwjpyhfvlpmnwzspefyunipjegskgfbvywgeyepikvdjiiihfvlknlqueuhjqdruiedmruivpeyipqnvliktlbokydvvldedvlrpgwswsiiefluromfcbzhjiunikwnygkvlrubknleyscgfqerpmlrxscuhfznzmqrbiipgrjqrojkydppdmvldplrxocpgfilpvlqwoqiyyeicijqeruiyybochgrssgllswnkqlfvldvhiwbromnejpwirydfgyeedmisnjqvqtjeyxkcrdschdtwocpfdaazayfsoximiwbvqtbysgginhqvqtaorrxmeoruydvzieiejeyqolwpscelpbqcydvwboqvwefrxzjeyqxlfilmqyfvcdkfrcrzdldhsqhtrzieihiucugfqerplhdmknjyflerxzfcoimjjcjvgwlmihwjqliknjswazamiybghgrgbzmirdedqsfvokhgrcofimfsqaqyjeyknnbvizdtbmnrtnqirzswnaocpbqemiielwsnhdnrynyfrwgrxzfvkdlsyenrtljeyfkvburphvnodbgwuembkmxbscumiwppofrjkmyjqdmphxiubxydvsovolrybhxhdzgrxzyempvejeyqvnlbrukwuybgkkeekkgmvvqkqhdjjvqtezqahgdljpxejeyfkvbyarxvnodrxwnkqcwliemcqqwwsnhgrebdkwubibgzqeviinbvldqmiwdmambbihlejeyjldbwazayrmqnkwuzsnhlqymugirmihmdvzjuijeyfzgxralrokrjscunqvldimiwdzxlbwqloprubwvjjwdpxeybqzhgrjscjjflocpnqvldokfjskqsrycuhgrjqrojaemdvsnjuvokfjskqwxwqeiyjbycpyrdadkybnqnafnpbprjewruelrvkoifvciahgrklqgfyuocgwdioqplqyuzxzybqugiwciallaybzxjqdruivyynlldqiocpldklkgprnqnafnpbprjewruudrcobkvbyarxzyezdotbexknlxbdromfybfyseuqcpnowoqmlbboilwrhqqxlswdpuyrwupyzndxdieybqztleyvhxedlrpuyryrfkwiykkmdiwoqhfnlqmllrdkpxeybqzhgrjxzvqrydnognongqwrvqiljwuqbnnxbjzifqeruayymihxdeybvqwrwnnihimbzhfdmscydvjldkyyvlphmiwlzafrexugfoyckonbvizopdznaqyiukakwxuqnkwubqukeyendkaruraqywydxiybxojiqrbscplswdvwincqgpdnjsnkpjcrdvvbwoiiepuruolswbnijwcmpgmfleromiwlzqsbexkgpralphnovdzaqwwkuqtwdvdkwramrxenaschgrwonhlelmplinpazayieynivnoupysnjedhmiwicihfvlbndtmihnjswnpaziwjmamqwfdvmiwicihfvlbndtmihnjswmdjmybqqipvcrmifnsqknnqikkvjqiqiyfdkddpnqcoihnyukrxdvjrdkybybggwybqnijnodxqefllrozeycrqtbvlrvfyasileeublafdznknluwmgvdkybghgrvqpvvnooqiqvvoavjlsqchdomihvzfybkolwpofqtybrukmbwqloqewogkwuyvigwubocpmiyruqiucruixvxxzvjybsqomjsihhgfpazahnongvnbwvhhjxovrhjaefdvjxwocpxnobkvvdljniiomihmdvzjrxerwjmixnsqxqewugdgsfaqqivnosbqtwdbzhsfljaktwvmrhgybqnijdvnzmmfdqrhnbyezqebbswkwueyqwjkvorxnbyviinyukzxijmihvfyeupwgybokgffljrodedqqognongydvcskaknlojldvdazahnongxdycqdhgrrihxedjaigwrrqkmlrlicixnobkvvdljpxdybqqxdevldddvljpvvbviciqrvmdiwdpoqejqdoakyturrojkurvydvkocxdycskaknlojldvdkdtlqkqchteuqnkzncqeiwpbskienhqnvdbwxqqpddqdjadzndyswmscumnvldownamugmrcyfenyexknlteychjflicidovldolswbfiwpbibkmxbqghgrpnrugycorpnbwqpdidkgnjdyebknlpubxqsybqniarlrupdswrzpjjvldjlnxndgwyboktjwzqvhlwziaolswbmljxgjztlbalzbirarzhgrcyfenyexknlblibypnobkknqubknldorhewfioknlewjplitmkzvynakpxeaodrieybqfgwtmepverlocphiwbpjyfzddhtelqgkwucpqgwlkofimnaqghgrwoqhgybqqizewmrxpjioqplqrqpamfpyibinaqqotqzslijwziknlepnzmlecocppjlqrugaednwjtwrzdlienghgrsocpmiwaplibysghdtwmuiwdorhewxeudojlysckmbwqggwlvsfihfznvqtqerxgarokzbmiwkdiebexknlbwxiqhrjkknjyaqfkviyfdhgrsscqteioqplqcskgffljdietukdvvfpsnhyrvcukwrspkygdljkqprlocpyrkqrtlqerugwlrykgmfclzjlwwknxlbcsagfyjqkwgdpyilgdljpxeoubgxdqwrzvlxwseinwebxbdewrdvwfvamixdokdhgrjqrogdznfilysahxheurkiwkeqfojqduvawkyschluxsjhtewkpvmfconhlkpdzewdvyqimnaoqpmiwscbnqurdkhnjgzbjevsnkpfcrjkyswjrxmnybrejlwqeiwybqukwucrukmtygdwynabnqsybiqxfdjqmimywdknjqujiigdljnqtesinhfdkddpmrydnxlswdnilzeyqivrcqeiyjsocgfybqgifxwbgkwyexdtlemgrxzdljdtlemkikarvlphlswdigardsahgriddkmljocpsdvldvdonqnafiyjlxdplmukmpykugeuwbbgmiubugppeyipgrliknjswkkqduubpmlnplrefrzxbkfybqiqarexoaedcuzhgrjianlecicllbcrukwybqiqarexfkyjpiqzlbokknlewoqimijqdeneyciifnpihvqeeruiycwkhownvadhyrkiqpluubknlaeilhgrpsqomyboknlpykpejqzslivnoocpprvldolxebghgdvldnjuykdxfrexuapnodpxeybqknnedrukmiwgcihiwmpojxebtaleedkndviljqwhoqqiexjyjgsfwjzxljeypvlxjyjgsfwjhjdqsauijevocpmiwbpgibvlphkfwdjivnodukwucpriyxwruihdznnqstmldkyyybghdtedqqhpbqckfyjoculexonolbraknnbiiiudybouihfzncqmzlibhgdvrbqqwwjuiyrbqbgiwdqdenyvlddinejzbdqwupxvnoupygdhquijediahgrrndofrduzawyyscgmfcruigfildomteychjflscqteaiqlebbihlejeyqijxbruifvsurhvnomzaiuboeidqzazxluwkrvldljknjyvigifxwbgkwurqbgmivlzolpbigmlwzschgrdqdjlbvfplirmrukmfcmuynyukjkiwwjknlazqnolusihxmdubdtlemruqtlbrrnjswsfjyfcicieflqyjyrckrqwfsynhsewqmypjdqdpfozoxgfiwniqoqocpudndnhwb"
p=list("****")
for i in range(26):
    p[0] = chr(ord('a') + i)
    for j in range(26):
        p[1] = chr(ord('a') + j)
        for k in range(26):
            p[2] = chr(ord('a') + k)
            for l in range(26):
                p[3] = chr(ord('a') + l)
                if (s.count("".join(p)) >= 20): #这里的20是可以调的，得到合适数量的四位字符串即可
                    print("".join(p)) #到此得到了几个在密文中重复了20次以上的串

#接下来选其一把它们在明文中的位置记录下来
def find_sub_n_index(str,substr,time):#自己写的算法，返回子字符串第n次出现时的下标
    begin=0
    while(str[begin:].find(substr)!=-1 and time>0):
        begin+=str[begin:].index(substr)+4#这里的4是因为选的子字符串长度为4
        time-=1
    return begin-4
position=[]
key="erui"
for i in range(1,20):
    site = find_sub_n_index(s, key, i)
    position.append(site)
get_gcd=[]#开始求间距的最小公倍数
for i in range(18):
    get_gcd.append(position[i+1]-position[i])
for i in range(2,min(get_gcd)):
    flag=1
    for j in range(18):
        if(get_gcd[j]%i!=0):
            flag=0
            break
        if(flag):
            gcd=i
print("一轮长度：",gcd)#一轮密钥长度为6


best_index=0.065
dic_index={'a': 0.08167,'b': 0.01492,'c': 0.02782,'d':0.04253,'e': 0.12702,'f':0.02228,'g': 0.02015,'h':0.06094,'i':0.06966,'j':0.00153,'k':0.00772,'l':0.04025,'m':0.02406,'n':0.06749,'o':0.07507,'p':0.01929,'q':0.00095,'r':0.05987,'s':0.06327,'t':0.09056,'u':0.02758,'v':0.00978,'w':0.02360,'x':0.00150,'y':0.01974,'z':0.00074}

import gmpy2
import math
def index_of_conincidence(c,i,j):#解密➕算重合指数
    fre=[0]*26
    sum=0
    for k in c:#解密➕算频率
        if(ord(k)-ord('a')-j>=0):
            k=chr(gmpy2.invert(i,26)*(ord(k)-ord('a')-j)%26+97)#模运算求逆就要用到逆元了
        else:
            k=chr(gmpy2.invert(i,26)*(ord(k)-ord('a')-j+26)%26+97)
        fre[ord(k)-ord('a')]+=1
    for k in range(26):
        sum+=(fre[k]/len(c))*dic_index[chr(ord('a')+k)]#这里和一般计算重合指数的方法不太相同，但实际上道理上是一样的。
    return sum
def find_key(c):
    index=1
    for i in range(26):#爆破乘数
        if(i%13==0 or i%2==0):#有相同因子的求不出逆元，解密后明文不唯一，必须舍弃
            continue
        for j in range(26):#爆破加数
             if(math.fabs(index_of_conincidence(c,i,j)-best_index)<index):#谁最接近0.065？
                 index=math.fabs(index_of_conincidence(c,i,j)-best_index)
                 key1=i
                 key2=j
    return (key1,key2)
t=[]
key3=[0]*6
key4=[0]*6
for i in range(6):#还原密钥
    temp="".join(["".join(s[cycle*6+i]) for cycle in range(len(s)//6)])
    t.append(temp)
    key3[i]=find_key(temp)[0]
    key4[i]=find_key(temp)[1]
for k in range(len(s)):#解密
        if(ord(s[k])-ord('a')-key4[k%6]>=0):
            k=chr(gmpy2.invert(key3[k%6],26)*(ord(s[k])-ord('a')-key4[k%6])%26+97)
        else:
            k=chr(gmpy2.invert(key3[k%6],26)*(ord(s[k])-ord('a')-key4[k%6]+26)%26+97)
        print(k,end="")
