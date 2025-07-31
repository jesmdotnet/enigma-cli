import argparse
from enigma import EnigmaMachine

def parse_args():
    parser = argparse.ArgumentParser(description="Enigma Machine CLI")
    parser.add_argument("message", help="The message to encrypt or decrypt (no quotes)")
    parser.add_argument("--mode", choices=["encrypt", "decrypt"], default="encrypt", help="Mode: encrypt or decrypt")
    return parser.parse_args()

def main():
    args = parse_args()

    rotor_settings = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II
        "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Rotor III
    ]
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    plugboard_settings = [('A', 'B'), ('C', 'D'), ('E', 'F')]

    enigma = EnigmaMachine(rotor_settings, reflector, plugboard_settings)

    result = enigma.encrypt(args.message.upper())
    print(result)

if __name__ == "__main__":
    main()
