key = int(input())
message = input()
message = list(message)
cipher = []
for charachter in message:
    cipher.append(chr(((ord(charachter) - 65 + key) % 26) + 65))
print (''.join(cipher))
