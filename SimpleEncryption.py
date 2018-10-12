
# Input: plain text and key as list of hexadecimal numbers.
# Fixed tables representing the Sbox and permutation layer.
# $Output: cipher text as a list of hexadecimal numbers.
def enc(plaintext, key):
  SBoxlist = [0x1, 0xa, 0x4, 0xc, 0x6, 0xf, 0x3, 0x9, 0x2, 0xd, 0xb, 0x7, 0x5, 0x0, 0x8, 0xe]
  permutationlayer = [0, 17, 34, 51, 48, 1, 18, 35, 32, 49, 2, 19, 16, 33, 50,
                      3, 4, 21, 38, 55, 52, 5, 22, 39, 36, 53, 6, 23, 20, 37, 54, 7,
                      8, 25, 42, 59, 56, 9, 26, 43, 40, 57, 10, 27, 24, 41, 58, 11,
                      12, 29, 46, 63, 60, 13, 30, 47, 44, 61, 14, 31, 28, 45, 62, 15]

  xorlayer = [None] * 16
  for i in range(len(plaintext)):
    xorlayer[i] = plaintext[i] ^ key[i]

  sboxlayer = [None] * 16
  for i in range(len(sboxlayer)):
    sboxlayer[i] = SBoxlist[int(xorlayer[i])]

  counter: int = 0
  cipherbits = [0] * 64
  for item in sboxlayer:
    itembits = bin(item)[2:].zfill(4)
    for i in itembits:
      cipherbits[counter] = i
      counter += 1

  cypherbitslayer = [0] * 64
  for i in range(len(cypherbitslayer)):
    cypherbitslayer[permutationlayer[i]] = cipherbits[i]
    #cypherbitslayer[i] = permutationlayer[cipherbits[i]]

  cypherhex = []
  for i in range(0,64,4):
    fourbits = "".join(cypherbitslayer[i:i+4])
    hexvalue = hex(int(fourbits,2))
    cypherhex.append(hexvalue)

  return cypherhex

normallist = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf]
print(normallist)

keylist = [0xc, 0x0, 0x1, 0x4, 0x5, 0x3, 0xe, 0x7, 0xf, 0x8, 0x9, 0xa, 0x2, 0xb, 0x6, 0xd]
print(keylist)

test = enc(normallist,keylist)
print(test)