import math
import base64

flag = "xm4s{this_is_dummy_flag}"
key = "paswd"
blocksize = len(key)
initial_vector = "abcde"
encrypted_flag_answer = b'aW4kYHpQUDt+dUVuC0tSamoWX0RjexFBT307HxUI'

# 足りない分は'#'で埋める
if len(flag)%blocksize != 0:
    flag+= '#' * (blocksize - len(flag)%blocksize)

print(f"flag: {flag}")
print(f"flag lenght: {len(flag)}")
print(f"block size: {blocksize}")

encrypted_flag = ""
last_enc = initial_vector

for i in range(0,len(flag),blocksize):
    asciicode = [ord(j) for j in flag[i:i+blocksize]]
    chain = [asciicode[j] ^ ord(last_enc[j]) for j in range(blocksize)]
    enc = [chain[j] ^ ord(key[j]) for j in range(blocksize)]
    enc = ''.join([chr(j) for j in enc])
    encrypted_flag += enc
    last_enc = enc

# 不可視文字だと扱いにくいのでbase64する
encrypted_flag = base64.b64encode(encrypted_flag.encode())

print("encrypted(your flag):",encrypted_flag)
print("encrypted(true flag):",encrypted_flag_answer)

if encrypted_flag != encrypted_flag_answer:
    print("Your flag is invalid!")
else:
    print("Your flag is right!")
