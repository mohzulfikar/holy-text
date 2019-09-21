ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#cracking the caesar encryption algorithm with brute-force
def caesar_crack(cipher_text):

	#we try all the possible key values so the size of the ALPHABET
	for key in range(len(ALPHABET)):
	
		#reinitialize this to be an empty string
		plain_text = ''
		
		#we just have to make a simple caesar decryption
		for c in cipher_text:
			index = ALPHABET.find(c)
			index = (index-key)%len(ALPHABET)
			plain_text = plain_text + ALPHABET[index]
			
		#print the actual decrypted string with the given key
		print('With key %s, the result is: %s'%(key,plain_text))

def crackCustom(cipher):
    
    #ASCII hanya 256 (bruteforce semua)
    for key in range(256):

        #declare plaintext to store
        plain = ''

        #simple cracking with loop
        for c in cipher:
            now = chr((ord(c) - key) % 256)
            plain = plain + now
        
        #print yg telah terdekripsi
        print(f'With the key = {key}, result = {plain}')


if __name__ == "__main__":	
    encrypted = 'VJKUBKUBCBOGUUCIG'
    caesar_crack(encrypted)
    enc = input('masukkan yang terenkripsi : ') 
    crackCustom(enc)
