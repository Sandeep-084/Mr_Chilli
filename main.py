ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets =[]
for i in ascii_letters:
    alphabets.append(i)
print(alphabets)



def encrypt(original_text,shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabets.index(letter)+ shift_amount % len(alphabets)
        cipher_text+=alphabets[shifted_position]
    return cipher_text



original_text = input("Enter the text: ")
shift_position = 5
encrypted_text = encrypt(original_text, shift_position)

print("Encrypted Text:", encrypted_text)