from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256  
 
#Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

#Simulated document content
original_document = b"This is original document conent."
modified_document = b"This is modified document content."

#Hash the document content
original_hash =  SHA256.new(original_document)
modified_hash =  SHA256.new(modified_document)

#Create a signature using the private key
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(original_hash)

#Verify the signature using the punlic key with the modified content
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(modified_hash, signature)
    print("Signature is valid.")
except(ValueError, TypeError):
    print("Signature is invalid.")
    
