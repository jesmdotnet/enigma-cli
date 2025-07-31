import string

class EnigmaMachine:
    def __init__(self, rotor_settings, reflector, plugboard_settings):
        self.alphabet = string.ascii_uppercase
        self.plugboard = self.setup_plugboard(plugboard_settings)
        self.rotors = self.setup_rotors(rotor_settings)
        self.reflector = self.setup_reflector(reflector)
        self.rotor_positions = [0, 0, 0]  # Initial rotor positions

    def setup_plugboard(self, settings):
        plugboard = {letter: letter for letter in self.alphabet}
        for pair in settings:
            a, b = pair
            plugboard[a], plugboard[b] = b, a
        return plugboard

    def setup_rotors(self, settings):
        return [list(wiring) for wiring in settings]

    def setup_reflector(self, wiring):
        return {self.alphabet[i]: wiring[i] for i in range(26)}

    def rotate_rotors(self):
        # Step rotor 1, handle cascading
        self.rotor_positions[0] = (self.rotor_positions[0] + 1) % 26
        if self.rotor_positions[0] == 0:  # If rotor 1 made a full rotation
            self.rotor_positions[1] = (self.rotor_positions[1] + 1) % 26
            if self.rotor_positions[1] == 0:  # If rotor 2 made a full rotation
                self.rotor_positions[2] = (self.rotor_positions[2] + 1) % 26

    def process_letter(self, letter):
        if letter not in self.alphabet:
            return letter  # Ignore non-alphabetic characters

        # Step 1: Plugboard substitution
        letter = self.plugboard[letter]

        # Step 2: Forward through rotors
        index = self.alphabet.index(letter)
        for i in range(3):  # Go through the rotors
            index = (index + self.rotor_positions[i]) % 26
            letter = self.rotors[i][index]
            index = self.alphabet.index(letter)

        # Step 3: Reflector
        letter = self.reflector[letter]

        # Step 4: Backward through rotors
        for i in reversed(range(3)):  # Go back through the rotors
            index = self.rotors[i].index(letter)
            index = (index - self.rotor_positions[i]) % 26
            letter = self.alphabet[index]

        # Step 5: Plugboard substitution
        letter = self.plugboard[letter]

        # Rotate rotors after processing one letter
        self.rotate_rotors()

        return letter

    def encrypt(self, message):
        result = []
        for letter in message.upper():
            result.append(self.process_letter(letter))
        return ''.join(result)

# Example Usage
if __name__ == "__main__":
    # Define rotor wirings, reflector, and plugboard settings
    rotor_settings = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II
        "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Rotor III
    ]
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  # Reflector B
    plugboard_settings = [('A', 'B'), ('C', 'D'), ('E', 'F')]  # Example pairs

    # Initialize the Enigma machine
    enigma = EnigmaMachine(rotor_settings, reflector, plugboard_settings)

    # Encrypt and decrypt a message
    message = "HELLO WORLD"
    encrypted_message = enigma.encrypt(message)
    print(f"Encrypted: {encrypted_message}")

    # Decrypting is the same process because of the reflector's symmetry
    enigma = EnigmaMachine(rotor_settings, reflector, plugboard_settings)
    decrypted_message = enigma.encrypt(encrypted_message)
    print(f"Decrypted: {decrypted_message}")
