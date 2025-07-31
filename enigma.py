# enigma.py

ROTOR_WIRINGS = {
    '1': "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I
    '2': "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II
    '3': "BDFHJLCPRTXVZNYEIWGAKMUSQO",  # Rotor III
}

REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def letter_to_index(letter):
    return ord(letter.upper()) - ord('A')


def index_to_letter(index):
    return ALPHABET[index % 26]


class Rotor:
    def __init__(self, wiring: str, start_pos: str):
        self.wiring = wiring
        self.position = letter_to_index(start_pos)

    def encrypt_forward(self, c):
        # Convert letter to index, offset by rotor position
        idx = (letter_to_index(c) + self.position) % 26
        mapped_char = self.wiring[idx]
        # Map back with reverse position offset
        out_idx = (letter_to_index(mapped_char) - self.position) % 26
        return index_to_letter(out_idx)

    def rotate(self):
        self.position = (self.position + 1) % 26


class EnigmaMachine:
    def __init__(self, rotor_order, start_positions):
        # rotor_order like ['1', '2', '3']
        # start_positions like ['A', 'B', 'C']
        self.rotors = [
            Rotor(ROTOR_WIRINGS[r], pos)
            for r, pos in zip(rotor_order, start_positions)
        ]
        self.reflector = REFLECTOR_B

    def encrypt(self, message):
        result = ""
        for char in message.upper():
            if char not in ALPHABET:
                result += char
                continue

            # Step rotors - rightmost rotor rotates every keypress
            self.rotors[-1].rotate()
            # Implement rotor turnover if needed - simplified here (only right rotor rotates)

            # Pass through rotors forward
            c = char
            for rotor in reversed(self.rotors):  # right to left
                c = rotor.encrypt_forward(c)

            # Reflector
            c = self.reflector[letter_to_index(c)]

            # Pass through rotors backward (reverse wiring)
            for rotor in self.rotors:  # left to right
                # Inverse map char through rotor wiring
                idx_in_wiring = rotor.wiring.index(c)
                c = index_to_letter((idx_in_wiring - rotor.position) % 26)

            result += c

        return result
