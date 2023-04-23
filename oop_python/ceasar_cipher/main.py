end = True
def caesar():
    new_index = []
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    direction = input("\nType 'encode' or 'decode' to encode or decode a message respectively:\n").lower()
    if not (direction == "encode" or direction == "decode"):
        print("\nPlease enter the right choice\n")
        return
    text = input("\nType your message:\n").lower()
    shift = int(input("\nEnter the shift amount:\n"))
    
    def new_index(old_index,shift, direction):
        new_Index = 0
        if direction == "encode":
            if old_index+shift > (len(letters)-1):
                new_Index = old_index+shift - (len(letters))
            else:
                new_Index = old_index+shift
                
        elif direction == "decode":
            if old_index-shift < 0:
                new_Index = old_index-shift + (len(letters))
            else:
                new_Index = old_index-shift
        return new_Index
    
    def cipher(text, shift):
        msg = ""
        text = text.split()
        for part in text:
            part = list(part)
            for letter in part:
                old_index = letters.index(letter)
                if direction == "encode":
                    index = new_index(old_index, shift, "encode")
                elif direction == "decode":
                    index = new_index(old_index, shift, "decode")
                msg += letters[index]
            msg += " "
        print(f"\nYour {direction}d message is '{msg.strip()}'")
    
    if direction == "encode" or direction == "decode":
        cipher(text, shift)
    else:
        print("\nYou eneterd a wrong choice plz start again")

while end:
    caesar()
    to_continue = input("\nType 'yes' to continue or 'no' to exit:\n").lower()
    if to_continue == "no":
        end = False
    elif not(to_continue == "yes" or to_continue == "no"):
        print("\nYou eneterd a wrong choice plz start again")
        break
