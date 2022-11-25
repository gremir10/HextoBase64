import codecs

"""Convert hex to base64 (hex string converted to bytes, bytes then encoded to base4 notation):
The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"""

hex_to_encode = input("input hex to be encoded in base64: ")

base64 = codecs.encode(codecs.decode(hex_to_encode, 'hex'), 'base64').decode()
print(base64)

''' partially-functional manually coded version:
#1. initialize variable(s) for base64 index table
ascii_lower = 'abcdefghijklmnopqrstuvwxyz'
ascii_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_digits = '0123456789'

base64alph = ascii_lower + ascii_upper + ascii_digits + '+/'

# input hex string
encode_this = input("input hex to encode in base64: ")

#1. break input up into 8-bit chunks:
#format(object, specifier) converts integer to binary and keeps leading 0s
#also use string.join(iterable)a, and encode('utf8')
encode_8bits = ''.join([format(bits, '08b') for bits in encode_this.encode()])

#2. split 8-bit chunks into 6-bit chunks, pad chunks with '0' at end if necessary
encode_6bits = [encode_8bits[bits:bits+6] for bits in range(0, len(encode_8bits), 6)]
padding = (6 - len(encode_6bits[len(encode_6bits)-1]))
encode_6bits[len(encode_6bits)-1] += padding * '0'

#3. convert 6-bit chunks to ASCII
#use int(bits, 2) to convert binary to decimal
after_encode = ''.join([base64alph[int(bits,2)] for bits in encode_6bits])
after_encode += int(padding / 2) * '='

print('The input after base64 encoding is: ')

print(after_encode)
'''


