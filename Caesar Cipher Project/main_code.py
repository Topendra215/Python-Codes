import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
will_continue=True
while will_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        def encrypt(original_text, shift_amount):

            cypher_text = ""
            for letters in original_text:
                position_of_letters = alphabet.index(letters)
                cypher_text += alphabet[(position_of_letters + shift_amount) % len(alphabet)]
            print(f"The Encoded Message is {cypher_text}")


        encrypt(original_text=text, shift_amount=shift)

    if direction == "decode":
        def decrypt(original_text, shift_amount):

            cypher_text = ""
            for letters in original_text:
                position_of_letters = alphabet.index(letters)
                cypher_text += alphabet[(position_of_letters - shift_amount) % len(alphabet)]
            print(f"The Decoded Message is {cypher_text}")


        decrypt(original_text=text, shift_amount=shift)

    again=input("\nYou want to Encode or Decode Again?\nType 'yes' if you want to go again otherwise type 'no':\n")

    if again=="no":
        will_continue= False
        print("Thank You")


