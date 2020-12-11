import mykeydef as key
from time import sleep
import binascii
import string
import os

private_key = 'Keys/private_key.pem'
public_key = 'Keys/public_key.pem'

#Make Key if not exist
if not os.path.exists(private_key):
  if not os.path.exists(public_key):
    key.genkeys()

#INPUT
text=input("Input Text/Encrypted Text: ")
if all(c in string.hexdigits for c in text) == True:
    #Decrypt
    keys=key.loadkeys(private_key,public_key)
    text = binascii.unhexlify(text)
    print("")
    print(key.mdecode(text,keys[1]).decode())
else:
    user = input("Username: ")
    user_public_key ='PubKeys/'+user+'.pem'

    if os.path.exists(user_public_key):
        print("")
        keys=key.loadkeys(private_key,user_public_key)
    else:
        print("User key Not Found!!!")
        print("Use Own Private Key")
        print("")
        keys=key.loadkeys(private_key,public_key)
        pass
    #Encrypt
    text = key.mencode(text,keys[0])
    print(binascii.hexlify(text).decode())
sleep(10)