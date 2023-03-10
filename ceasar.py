alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#function that encrypts or decrypts a text by shifting the letters 
def ceasar(plain_text, shift_amount, direction):
  cypher_text=""
  if direction != "decode" or direction != "encode":
    print("Error. Restart the program.")
  else:
    if direction == "decode":
        shift_amount *= (-1)
    for letter in plain_text:
      if letter not in alphabet:
        cypher_text += letter
      else:
        position = alphabet.index(letter)
        new_position = (position+shift_amount)%26
        new_letter = alphabet[new_position]
        cypher_text+=new_letter
    print(f"The {direction}d text is: {cypher_text}.")
#call the function
ceasar(text,shift,direction)