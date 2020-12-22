import math
import base64

flag = "xm4s{I_like_CBC_encryption!}"
key = "paswd"
blocksize = len(key)
initial_vector = "abcde"

encrypted_flag = base64.b64decode(b'aW4kYHpQUDt+dUVuC0tSamoWX0RjexFBT307HxUI').decode()

last_enc = initial_vector

decrypted_flag = ""

for i in range(0,len(flag),blocksize):
    asciicode = [ord(j) for j in encrypted_flag[i:i+blocksize]]
    dec = [asciicode[j] ^ ord(key[j]) for j in range(blocksize)]
    chained = [dec[j] ^ ord(last_enc[j]) for j in range(blocksize)]
    chained = ''.join([chr(j) for j in chained])
    decrypted_flag += chained
    last_enc = encrypted_flag[i:i+blocksize]

print(decrypted_flag)
