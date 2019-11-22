#Python3
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#metode brute-force
def caesar_crack(cipher_text):

	# coba semua kemungkinan dalam alfabet
	for key in range(len(ALPHABET)):
	
		#inisialisasi plaintext kosong
		plain_text = ''
		
		#decrypting dengan kunci = variabel key
		for c in cipher_text:
			index = ALPHABET.find(c)
			index = (index-key)%len(ALPHABET)
			plain_text = plain_text + ALPHABET[index]
			
		#print string yang telah terdekripsi
		print('With key %s, the result is: %s'%(key,plain_text))

def crackCustom(cipher):
    
    #ASCII hanya 256 (bruteforce semua)
    for key in range(256):

        #inisialisasi plaintext kosong
        plain = ''

        #simple cracking dengan perulangan
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
