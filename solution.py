# solution.py
#check the operators

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr(ord(char) - start + shift % 26 + start)
        else:
            result += char
    return result

def swap_and_encrypt(scroll1, scroll2, lunar_phase):
    # Swap scrolls using tuple assignment
    scroll1, scroll2 = scroll2, scroll1
    
    # Encrypt each scroll with the Caesar cipher using opposite shifts
    shift1 = lunar_phase
    shift2 = -lunar_phase
    
    encrypted_scroll1 = caesar_cipher(scroll1, shift1)
    encrypted_scroll2 = caesar_cipher(scroll2, shift2)
    
    return encrypted_scroll1, encrypted_scroll2

