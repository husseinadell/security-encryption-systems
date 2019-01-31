import math
key_length = int(input())
key_dim = int(math.sqrt(key_length))
key = input().split()
key = [int(i) for i in key]  # using list Comprehension to convert array of chars to arr of ints
message = list(input())  # holds the values of message
while len(message) % key_dim != 0:
    message.append("X")
# using list Comprehension to create list of lists row*row
key_matrix = [[0] * key_dim for row in range(key_dim)]
results = []
k = 0
for i in range(key_dim):  # iterating to fill the key matrix
    for j in range(key_dim):
        key_matrix[i][j] = key[k]
        k += 1
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0, len(message), key_dim):
    message_slice = [[ord(item) - 65] for item in message[i:key_dim+i]
                     ]  # slice and convert message to be vector
    result = [[sum(a*b for a, b in zip(X_row, Y_col))
               for Y_col in zip(*message_slice)] for X_row in key_matrix]  # matrix multiplication using list Comprehension
    results += result
flatten_result = [letters[item % 26]
                  for sub in results for item in sub]  # converting list of lists to a flatten list
print(''.join(flatten_result))
