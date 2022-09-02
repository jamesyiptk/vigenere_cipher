from sys import argv

def create_key(keyword, letter):
    key = list(keyword)
    if len(letter) == len(key):
        return key
    else:
        for i in range(len(letter) - len(key)):
            key.append(key[i])
    return "".join(key)

def encrypt(key, letter):
    encrypt_text = [chr((ord(letter[i]) + ord(key[i])) % 26 + ord('A')) for i in range(len(letter))]
    return "".join(encrypt_text)

def decrypt(key, encrypt_text):
    decrypt_text = [chr((ord(encrypt_text[i]) - ord(key[i]) + 26) % 26 + ord('A')) for i in range(len(encrypt_text))]
    return "".join(decrypt_text)

def main():
    if len(argv) < 4:
        print("Please enter the right amount of arguments")
        return

    keyword = argv[1]
    if "-d" in argv:
        infile = argv[3]
        outfile = argv[4]
        f_in_decrypt = open(infile, "r")
        encrypted_letter = f_in_decrypt.read().upper()
        f_out_decrypt = open(outfile, 'w')
        key = create_key(keyword, encrypted_letter)
        encrypt_text = decrypt(key, encrypted_letter)
        f_out_decrypt.write(encrypt_text)
        f_in_decrypt.close()
        f_out_decrypt.close()
    else:
        infile = argv[2]
        outfile = argv[3]
        f_in_encrypt = open(infile, "r")
        original_letter = f_in_encrypt.read().upper()
        f_out_encrypt = open(outfile, 'w')
        key = create_key(keyword, original_letter)
        encrypt_text = encrypt(key, original_letter)
        f_out_encrypt.write(encrypt_text)
        f_in_encrypt.close()
        f_out_encrypt.close()


if __name__ == '__main__':
    main()
