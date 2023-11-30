# Dictionary containing the codes for each letter
codes = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8', 'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5', 'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2', 'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y', 'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v', 'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s', 'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p', 'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m', 'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j', '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g', '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d', '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a', ':':',',',':':','?':'.','.':'?','<':'>','>':'<', "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=', '{':'[','[':'{','}':']',']':'}'}

def encrypt_file(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    encrypted_text = ''
    for char in text:
        if char in codes:
            encrypted_text += codes[char]
        else:
            encrypted_text += char  # For characters not in the dictionary, keep them unchanged

    with open(output_file, 'w') as file:
        file.write(encrypted_text)

def decrypt_file(input_file):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()

    decrypted_text = ''
    for char in encrypted_text:
        for key, value in codes.items():
            if char == value:
                decrypted_text += key
                break
        else:
            decrypted_text += char  # For characters not in the dictionary, keep them unchanged

    print("The decrypted output is:\n")
    print(decrypted_text)

def main():
    input_file = input("Enter the name of the input text file: ")
    output_file = input("Enter the name of the output file to save encrypted text: ")

    encrypt_file(input_file, output_file)

    encrypted_input_file = input("Enter the name of the encrypted input file: ")
    decrypt_file(encrypted_input_file)

if __name__ == "__main__":
    main()
