print('''
      
  ███████████████████████████████████████████████████████████████████████
  █─▄▄▄─██▀▄─██▄─▄▄─█─▄▄▄▄██▀▄─██▄─▄▄▀███─▄▄▄─█▄─▄█▄─▄▄─█─█─█▄─▄▄─█▄─▄▄▀█
  █─███▀██─▀─███─▄█▀█▄▄▄▄─██─▀─███─▄─▄███─███▀██─███─▄▄▄█─▄─██─▄█▀██─▄─▄█
  ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▀▄▀▄▀▄▄▄▄▄▀▄▄▀▄▄▀
     
      ''')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_task="Yes"
while end_task=="Yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift =shift % 25
  
  def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
      if letter not in alphabet:
        end_text += letter
      else :  
        position = alphabet.index(letter)
        if cipher_direction == "decode":
          shift_amount = -abs(shift_amount)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The {direction}d text is {end_text}")
   
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  end_task=input("Type 'Yes' to go again ,otherwise type 'No'\n")
  if end_task=="No":
    break
print("Thanks for using 'CAESAR CIPHER' ,Have a nice day!")   
