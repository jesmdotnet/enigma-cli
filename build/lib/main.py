import argparse
from enigma import EnigmaMachine

DEFAULT_ROTORS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Rotor III
]

DEFAULT_REFLECTOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
DEFAULT_PLUGBOARD = [('A', 'B'), ('C', 'D'), ('E', 'F')]

def parse_args():
    parser = argparse.ArgumentParser(description="Enigma Machine CLI")
    parser.add_argument("message", help="The message to encrypt or decrypt")
    parser.add_argument("--mode", choices=["encrypt", "decrypt"], default="encrypt", help="Mode")
    parser.add_argument("--rotors", nargs=3, metavar=('ROTOR1', 'ROTOR2', 'ROTOR3'),
                        help="Rotor wirings (3 strings, 26 characters each)")
    return parser.parse_args()

def main():
    args = parse_args()

    rotors = args.rotors if args.rotors else DEFAULT_ROTORS

    enigma = EnigmaMachine(
        rotor_settings=rotors,
        reflector=DEFAULT_REFLECTOR,
        plugboard_settings=DEFAULT_PLUGBOARD
    )

    result = enigma.encrypt(args.message.upper())
    print(result)

if __name__ == "__main__":
    main()
