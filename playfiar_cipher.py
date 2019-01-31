input_key = str(input()).replace('J', 'I')
message = str(input()).replace('J', 'I')
# print(input_key)
# build the encryption table.
letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
key = []
for char in input_key:
    if char not in key:
        key.append(char)
# print(key)
encryption_string = key
for charachter in letters:
    if charachter not in key:
        encryption_string.append(charachter)
# print(encryption_string)
key_matrix = [[0] * 5 for i in range(5)]
k = 0
for i in range(5):  # iterating to fill the key matrix
    for j in range(5):
        key_matrix[i][j] = encryption_string[k]
        k += 1
# print(key_matrix)
# tokenize the message
# for i in range(0, len(message), 2):
i = 0
while i < (len(message) - 1):
    if message[i] == message[i+1]:
        if message[i] == "X":
            message = message[:i + 1] + 'Q' + message[i + 1:]
        else:
            message = message[:i + 1] + 'X' + message[i + 1:]
    i += 2
if len(message) % 2 != 0:
    if message[-1] == 'X':
        message += "Q"
    else:
        message += "X"
# print(message)
# generate encryption
encrepted_message = []
for i in range(0, len(message), 2):
    r1 = c1 = 0
    r2 = c2 = 0
    # find location of each pair in key_matrix
    for r in range(5):
        for c in range(5):
            if key_matrix[r][c] == message[i]:
                r1 = r
                c1 = c
            if key_matrix[r][c] == message[i+1]:
                r2 = r
                c2 = c
    if r1 == r2:
        encrepted_message.append(key_matrix[r1][(c1 + 1) % 5])
        encrepted_message.append(key_matrix[r2][(c2 + 1) % 5])
    elif c1 == c2:
        encrepted_message.append(key_matrix[(r1 + 1) % 5][c1])
        encrepted_message.append(key_matrix[(r2 + 1) % 5][c2])
    else:
        encrepted_message.append(key_matrix[r1][c2])
        encrepted_message.append(key_matrix[r2][c1])

print(''.join(encrepted_message))
