from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

def genkeys():
#Gen Key Pair
 private_key = rsa.generate_private_key(
  public_exponent=65537,
  key_size=4096,
  backend=default_backend()
 )
 public_key = private_key.public_key()
#Store Private Key
 pem = private_key.private_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PrivateFormat.PKCS8,
  encryption_algorithm=serialization.NoEncryption()
 )
 with open('Keys/private_key.pem', 'wb') as f:
  f.write(pem)
#Store Public Key
 pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
 )
 with open('Keys/public_key.pem', 'wb') as f:
    f.write(pem)
 return

def loadkeys(private_key, public_key):
 with open(private_key, "rb") as key_file:
  private_key = serialization.load_pem_private_key(
   key_file.read(),
   password=None,
   backend=default_backend()
  )
 with open(public_key, "rb") as key_file:
  public_key = serialization.load_pem_public_key(
   key_file.read(),
   backend=default_backend()
  )
 return public_key,private_key

def mencode(message, public_key):
 message = message.encode()
 encrypted = public_key.encrypt(
  message,
  padding.OAEP(
   mgf=padding.MGF1(algorithm=hashes.SHA256()),
   algorithm=hashes.SHA256(),
   label=None
  )
 )
 return encrypted

def mdecode(encrypted, private_key):
 original_message = private_key.decrypt(
   encrypted,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
 )
 return original_message