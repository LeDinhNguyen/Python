alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

k = int(input("Enter the number k = "))
string = input("Enter a string: ")

def Encryption(string: str, k: int) -> str:
    encrypted_string = " "

    for char in string:
        if char == " ":
            encrypted_string += " "
        else:
            char_number = alpha.index(char.lower())
            encrypted_number = (char_number + k) % 26
            encrypted_string += alpha[encrypted_number]
    
    return encrypted_string

def Decryption(string: str, k: int) -> str:
    decrypted_string = " "

    for char in string:
        if char == " ":
            decrypted_string += " "
        else:
            char_number = alpha.index(char.lower())
            decrypted_number = (char_number - k) % 26
            decrypted_string += alpha[decrypted_number]
    
    return decrypted_string

print(Encryption(string, k))
print(Decryption(string, k))