import art

print(art.logo)

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(msg, shift):
    encoded_msg = []
    for i in msg:
        chars_relate_index = chars.index(i) + shift
        # if chars_relate_index >= len(chars): #only true for shift is <= last index.chars + last index.chars
        # so use while loop
        while chars_relate_index >= len(chars):
            chars_relate_index -= len(chars)
        encoded_msg.append(chars[chars_relate_index])

    print(f"The encrypted message is: {''.join(encoded_msg)}")

def decode(msg, shift):
    decoded_msg = ""
    for letter in msg:
        chars_relate_index = chars.index(letter) - shift
        chars_relate_index %= len(chars) #math formula to wrap around, just google it
        decoded_msg += chars[chars_relate_index] #using str "" instead of list to store, so no append

    print(f"The decrypted message is: {decoded_msg}") #no join due to it not being a list

restart = True

while restart:
    mode = input("Choose operation: type 'encode' to encrypt the message, or 'decode' to decrypt it.\n").lower()
    msg = input("Enter the message you want to encrypt or decrypt:\n").lower()
    shift = int(input("Enter the shift number (how many positions to move each letter in the alphabet):\n"))

    if mode == "encode":
        encode(msg, shift)
    elif mode == "decode":
        decode(msg, shift)

    continue_cipher = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if continue_cipher == "no":
        restart = False
        print("ciao")