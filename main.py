# main.py
import argparse
from enigma import EnigmaMachine


def parse_args():
    parser = argparse.ArgumentParser(description="Enigma Machine CLI")

    parser.add_argument(
        "message", help="Message to encrypt or decrypt (letters and spaces)"
    )
    parser.add_argument(
        "--rotors",
        nargs=3,
        choices=["1", "2", "3"],
        default=["1", "2", "3"],
        help="Rotor order, 3 rotors chosen from 1, 2, 3 (default: 1 2 3)",
    )
    parser.add_argument(
        "--start-positions",
        nargs=3,
        default=["A", "A", "A"],
        help="Starting letter positions for the 3 rotors (default: A A A)",
    )
    parser.add_argument(
        "--mode",
        choices=["encrypt", "decrypt"],
        default="encrypt",
        help="Mode (encrypt or decrypt), symmetric in Enigma",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    enigma = EnigmaMachine(args.rotors, args.start_positions)
    output = enigma.encrypt(args.message)

    print(output)


if __name__ == "__main__":
    main()
