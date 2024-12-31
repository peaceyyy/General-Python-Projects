import time
import simpleaudio as sa

morse_to_alphabet = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': "'",
    '-.-.--': '!',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-': '$',
    '.--.-.': '@'
   
}


def alpha_to_morse(string: str) -> str:
    morse_string = ""
    for char in string:
        if char == " ":
            morse_string += "/ "
        else:
            for key, value in morse_to_alphabet.items():
                if char.upper() == value:
                    morse_string += key + " "
    return morse_string.strip()

def play_sound(morse_code):

    dot_sound = sa.WaveObject.from_wave_file("C:/Users/Peace/Documents/vscode/Python/General Python Projects/Custom Morse Code/ding.wav")
    dash_sound = sa.WaveObject.from_wave_file("C:/Users/Peace/Documents/vscode/Python/General Python Projects/Custom Morse Code/meow.wav")    
    for symbol in morse_code:
        if symbol == '.':
            play_obj = dot_sound.play()
            play_obj.wait_done()  
        elif symbol == '-':
            play_obj = dash_sound.play()
            play_obj.wait_done()  
        elif symbol == '/':
            time.sleep(0.5)  
        time.sleep(0.2)  
def morse_to_alpha(string: str):
    result = ""
    for char in string.split(" "):
        if char == "":
            result += " "
        else:
            if char in morse_to_alphabet:
                result += morse_to_alphabet[char]
    return result.strip()

def get_str(prompt):
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("Invalid Input! Please enter a valid string.\n")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid Input! Please enter a valid integer.\n")

def main():
    while True:
        print("\nWelcome to Morse Code Translator")
        print("1. Alphabet to Morse Code")
        print("2. Morse Code to Alphabet\n")
        
        choice = get_int("Enter your choice: ")
        
        if choice == 1:
            string = get_str("Enter the string you want to convert to Morse Code: ")
            morse_code = alpha_to_morse(string)
            print("Morse Code:", morse_code)
            play_sound(morse_code)
            break
        
        elif choice == 2:
            string = get_str("Enter the Morse Code you want to convert to Alphabet: ")
            result = morse_to_alpha(string)
            print("Alphabet:", result)
            break
        
        else:
            print("Invalid Choice! Please enter a valid choice.")


if __name__ == "__main__":
    main()