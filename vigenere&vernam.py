key = input()
message = list(input())
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
generated_key = key
vigenere = []
vernam = []
while len(message) > len(generated_key):
    generated_key = generated_key + key
for i in range(len(message)):
    x = ((ord(message[i]) - 65) + (ord(generated_key[i]) - 65)) % 26
    vigenere.append(letters[x])
print ("Vigenere:", ''.join(vigenere))
for i in range(len(message)):
    x = (ord(message[i]) ^ ord(generated_key[i]))
    vernam.append("{:02x}".format(x).upper())
print ("Vernam:", ''.join(vernam))
if len(key) == len(message):
    print ("One-Time Pad: YES")
else:
    print ("One-Time Pad: NO")
