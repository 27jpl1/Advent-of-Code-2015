import hashlib

key = "iwrupvqb"
num = 0
hash_key = key + str(num)
hash_object = hashlib.md5(hash_key.encode())
hex_digest = hash_object.hexdigest()
while hex_digest[0:5] != "00000":
    num += 1
    hash_key = key + str(num)
    hash_object = hashlib.md5(hash_key.encode())
    hex_digest = hash_object.hexdigest()

print(num)
