import random
import string

word=" "+string.punctuation + string.digits + string.ascii_letters
word=list(word)
key=word.copy()

random.shuffle(key)

#print(f"word:{word}")
#print(f"key:{key}")


#Encrypt  code
txt=input("Enter a message for encryption:")
cipher=""

for a in txt:
    i=word.index(a)
    cipher+=key[i]

print(f"Original Message:{txt}")
print(f"Encrypted Message:{cipher}")

#Decrypt  code
cipher=input("Enter a message for decryption:")
txt=""

for a in cipher:
    i=key.index(a)
    txt+=word[i]

print(f"Encrypted Message:{cipher}")
print(f"Decrypted Message:{txt}")