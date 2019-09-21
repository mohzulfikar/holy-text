ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

#caesar encryption algorithm
def caesar_encrypt(plain_text):
	#encrypted message
	cipher_text = ''
	#case insensitive
	plain_text = plain_text.upper()
	
	#consider all the letters in the plain_text
	for c in plain_text:
		#numerical representation (index) associated with that character in the alphabet
		index = ALPHABET.find(c)
		#caesar encryption is just a simple shift of characters according to the key
		#use modular arithmetic to transform the values within the range [0,num_of_letters_in_alphabet]
		index = (index+KEY)%len(ALPHABET)
		#keep appending the encrypted character to the cipher_text
		cipher_text = cipher_text + ALPHABET[index]
		
	return cipher_text
	
	
def caesar_enc2(message , k):
    #message (case sensitive)
    plainTxt = message
    #cipherText
    cipherTxt = ''
    for c in plainTxt:
        indeks = chr((ord(c) + k) %  256)
        cipherTxt = cipherTxt + indeks

    return cipherTxt

def caesar_decrypt(cipher_text):

	plain_text = ''
	
	for c in cipher_text:
		index = ALPHABET.find(c)
		index = (index-KEY)%len(ALPHABET)
		plain_text = plain_text + ALPHABET[index]
		
	return plain_text
	
if __name__ == "__main__":
    msg = "Workshop Security Beginner" 
    encrypted = caesar_encrypt(msg)
    print(encrypted)
    print(f'Message yg akan dienkripsi: {msg}\nSetelah dienkripsi: {encrypted}')
    # custom
    m = "As always, Wikipedia describes it best: In computer security, Capture the Flag (CTF) is a computer security competition."
    enc = caesar_enc2(m, KEY)
    print(f'Message : {m}\nsetelah dienkripsi (algo 2): {enc}')
    txt = input('Masukan teks custom : ')
    k = int(input('masukan key : '))
    enc = caesar_enc2(txt, k)
    print(f'Setelah terenkripsi {enc}')
#    dec = caesar_decrypt(enc)
#    print(dec)
	
