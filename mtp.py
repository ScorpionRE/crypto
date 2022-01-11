#!/usr/bin/env python
import string
import collections
import sets


# XORs two string
def strxor(a, b):  # xor two strings (trims the longer input)
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])


# 10 unknown ciphertexts (in hex format), all encrpyted with the same key
c1 = "1e5d4c055104471c6f234f5501555b5a014e5d001c2a54470555064c443e"
c2 = "235b4c0e590356542a130a4242335a47551a590a136f1d5d4d440b095677"
c3 = "3613180b5f184015210e4f541c075a47064e5f001e2a4f711844430c473e"
c4 = "2413011a100556153d1e4f45061441151901470a196f035b0c4443185b32"
c5 = "2e130806431d5a072a46385901555c5b550a541c1a2600564d5f054c453e"
c6 = "32444c0a434d43182a0b1c540a55415a550a5e1b0f613a5c1f10021e5677"
c7 = "3a5a0206100852063c4a18581a1d15411d17111b052113460850104c4722"
c8 = "39564c0755015a13271e0a55553b5a47551a54010e2a06130b5506005a39"
c9 = "3013180c100f52072a4a1b5e1b165d50064e411d0521111f235f114c4736"
c10 = "2447094f10035c066f19025402191915110b4206182a544702100109133e"
ciphers = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
# The target ciphertext we want to crack
target_cipher = "49380d773440222d1b421b3060380c3f403c3844791b202651306721135b6229294a3c3222357e766b2f15561b35305e3c3b670e49382c295c6c170553577d3a2b791470406318315d753f03637f2b614a4f2e1c4f21027e227a4122757b446037786a7b0e37635024246d60136f7802543e4d36265c3e035a725c6322700d626b345d1d6464283a016f35714d434124281b607d315f66212d671428026a4f4f79657e34153f3467097e4e135f187a21767f02125b375563517a3742597b6c394e78742c4a725069606576777c314429264f6e330d7530453f22537f5e3034560d22146831456b1b72725f30676d0d5c71617d48753e26667e2f7a334c731c22630a242c7140457a42324629064441036c7e646208630e745531436b7c51743a36674c4f352a5575407b767a5c747176016c0676386e403a2b42356a727a04662b4446375f36265f3f124b724c6e346544706277641025063420016629225b43432428036f29341a2338627c47650b264c477c653a67043e6766152a485c7f33617264780656537e5468143f305f4537722352303c3d4379043d69797e6f3922527b24536e310d653d4c33696c635474637d0326516f745e610d773340306621105a7361654e3e392970687c2e335f3015677d4b3a724a4659767c2f5b7c16055a126820306c14315d6b59224a27311f747f336f4d5974321a22507b22705a226c6d446a37375761423a2b5c29247163046d7e47032244377508300751727126326f117f7a38670c2b23203d4f27046a5c5e1532601126292f577776606f0c6d0126474b2a73737a41316362146e581d7c1228717664091c"

# To store the final key
final_key = [None] * 150
# To store the positions we know are broken
known_key_positions = set()

# For each ciphertext
for current_index, ciphertext in enumerate(ciphers):

    counter = collections.Counter()
    # for each other ciphertext
    for index, ciphertext2 in enumerate(ciphers):
        if current_index != index:  # don't xor a ciphertext with itself
            for indexOfChar, char in enumerate(
                    strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))):  # Xor the two ciphertexts
                # If a character in the xored result is a alphanumeric character, it means there was probably a space character in one of the plaintexts (we don't know which one)
                if char in string.printable and char.isalpha(): counter[
                    indexOfChar] += 1  # Increment the counter at this index
    knownSpaceIndexes = []

    # Loop through all positions where a space character was possible in the current_index cipher
    for ind, val in counter.items():
        # If a space was found at least 7 times at this index out of the 9 possible XORS, then the space character was likely from the current_index cipher!
        if val >= 7: knownSpaceIndexes.append(ind)
    # print knownSpaceIndexes # Shows all the positions where we now know the key!

    # Now Xor the current_index with spaces, and at the knownSpaceIndexes positions we get the key back!
    xor_with_spaces = strxor(ciphertext.decode('hex'), ' ' * 150)
    for index in knownSpaceIndexes:
        # Store the key's value at the correct position
        final_key[index] = xor_with_spaces[index].encode('hex')
        # Record that we known the key at this position
        known_key_positions.add(index)

# Construct a hex key from the currently known key, adding in '00' hex chars where we do not know (to make a complete hex string)
final_key_hex = ''.join([val if val is not None else '00' for val in final_key])
# Xor the currently known key with the target cipher
output = strxor(target_cipher.decode('hex'), final_key_hex.decode('hex'))
# Print the output, printing a * if that character is not known yet
print(''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)]))

'''
Manual step
'''
# From the output this prints, we can manually complete the target plaintext from:
# The secuet-mes*age*is: Wh** usi|g **str*am cipher, nev***use th* k*y *ore than onc*
# to:
# The secret message is: When using a stream cipher, never use the key more than once

# We then confirm this is correct by producing the key from this, and decrpyting all the other messages to ensure they make grammatical sense
target_plaintext = "The secret message is: When using a stream cipher, never use the key more than once"
print(target_plaintext)
key = strxor(target_cipher.decode('hex'), target_plaintext)
for cipher in ciphers:
    print(strxor(cipher.decode('hex'), key))
