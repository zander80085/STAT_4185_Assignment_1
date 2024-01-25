encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

def decryption(encrypted_message):
    end = len(encrypted_message) 
    temp = list(encrypted_message)
    for i in range(1, end // 2, 2):
        temp[i], temp[end-i-1] = temp[end-i-1], temp[i]
    return "".join(temp)

print(decryption(encrypted_message))


