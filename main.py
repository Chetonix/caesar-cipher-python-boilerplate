from art import logo

print(logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    #create an empty string that will contain the encoded or decoded message

    #make shift amount remain under 1 to 26 value
    shift_amount %= 26
    #if cipher_direction == "decode" multiply shift_amount by -1.
    


    for char in start_text:
        #if char not in alphabet, add it to the string(from above) as it is 
        


        #else
            #find the position of the char in alphabet list, add it a shift_amount and put that newly positioned alphabet in the string(from above)
            

    #print a message including the string (from above)




continue_program = 'yes'

while (continue_program == 'yes'):
    continue_program = 'no'
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    continue_program = input(
        "Do you want to restart the cipher program? yes or no: ").lower()


