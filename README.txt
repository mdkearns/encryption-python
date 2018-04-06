-----------------------------------------------------------------------------

Author: Matthew Kearns
Date: April 5th, 2018

Simple python script used to learn encryption with Python's Crypto package.

-----------------------------------------------------------------------------

The encrypt.py program can be used to encrypt and decrypt both files and strings.

1. Using secret_string(message, public_key):
	
	- message is the user-supplied string to be encrypted.
	- public_key is the user-supplied public key to be used to encrypt the message.
	
	Users with access to the corresponding decryptor can decrypt messages encrypted with this public key.
	
2. Using enc_file(file_name, sym_key) and decrypt_file(file_name, sym_key):

	- file_name is the user-supplied file via a command line argument to the script.
	- sym_key is the symmetric key that can be used to both encrypt and decrypt files.
	
		Example Usage:
				
				python encrypt.py file_to_be_encrypted
				
		This results in the creation of two files: file_to_be_encrypted.enc and DECfile_to_be_encrypted.
		file_to_be_encrypted.enc is not human-readable, and its contents will appear to be gibberish to 
		the human eye. Decrypting this file with the provided symmetric key results in DECfile_to_be_encrypted,
		which is identical to the original file.
			
	
*NOTE: modifications to the main() function are most likely necessary to adapt the program to your specific needs.
	
This program relies on using a recent version of python3 and the cypto python package (pip install crypto).
