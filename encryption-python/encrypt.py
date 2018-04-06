"""
	File:       encrypt.py
	Author:     Matt Kearns (mdk2mc)
	Date:       10/10/2017
"""

__author__ = "mdk2mc"

import sys
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256

def secret_string(message, public_key):
	""" 
		secret_string returns the message encrypted with the 
		supplied public key. 
	"""
	encryptor = PKCS1_OAEP.new(public_key)
	return encryptor.encrypt(str.encode(message))

def enc_file(file_name, sym_key):
	""" 
		enc_file encodes the given file using the symmetric 
		key in a file called file_name.enc 
	"""
	success = False
	with open(file_name, 'rb') as f_in:
		output_file = file_name + ".enc"
		with open(output_file, 'wb') as f_out:
			while True:
				file_contents = f_in.read()
				if len(file_contents) == 0: 
					break
				sym_key_hash = SHA256.new(sym_key.encode())
				key_size8 = sym_key_hash.digest()[0:8]
				cipher = ARC4.new(key_size8)
				encrypted_contents = cipher.encrypt(file_contents)
				f_out.write(encrypted_contents)
				success = True
	return success

def decrypt_file(file_name, sym_key):
	""" 
		decrypt_file decodes the given file using the 
		symmetric key in a file called DECfile_name 
		(without .enc at the end) 
	"""
	success = False
	with open(file_name, 'rb') as f_in:
		if file_name[-4:] != '.enc':
			return success
		output_file = "DEC" + file_name[:-4]
		with open(output_file, 'wb') as f_out:
			while True:
				file_contents = f_in.read()
				if len(file_contents) == 0:
					break
				sym_key_hash = SHA256.new(sym_key.encode())
				key_size8 = sym_key_hash.digest()[0:8]
				cipher = ARC4.new(key_size8)
				f_out.write(cipher.decrypt(file_contents))
				success = True
	return success

def main():
    # secret_message = 'my secret message'
    # print("Secret Message:", secret_message)
    # random_generator = Random.new().read
    # key = RSA.generate(1024, random_generator)
    # pub_key = key.publickey()
    # encrypted_message = secret_string(secret_message, pub_key)
    # print("Encrypted Message:", encrypted_message)
    # decryptor = PKCS1_OAEP.new(key)
    # decrypted = decryptor.decrypt(encrypted_message)
    # print("Decrypted Message:", decrypted.decode())
    file_to_encrypt = sys.argv[1]
    print(enc_file(file_to_encrypt, 'my very long password'))
    print(decrypt_file(file_to_encrypt + ".enc", 'my very long password'))
		
if __name__ == '__main__':
    main()