# Enigma CLI

A Python-based simulation of the WWII Enigma Machine.

## Install
1. git clone https://github.com/YOUR_USERNAME/enigma-cli.git
   cd enigma-cli
Via Pip in venv, i need to add venv to git ignore.
2.  -m venv venv
source venv/bin/activate
3. pip install .

## Roadmap
1 - Customisable rotors
2 - Back out the Customisable rotors and add just a start letter, per rotor (I think this is closer to original functionality?)
3 - Other Customeisable settings - eg plugboard
4 - Calendar based rotor settings

## Instructions
1 - Use enigma-cli 'message'
or enigma-cli encrypt "HELLO WORLD"
also enigma-cli decrypt 'message'


## #roadmap1 - Customisable Rotors
3 - adds option to customise rotors per message
("--rotors", nargs=3, metavar=('ROTOR1', 'ROTOR2', 'ROTOR3'),
                        help="Rotor wirings (3 strings, 26 characters each)")

eg
enigma-cli "HELLO" --rotors QWERTYUIOPASDFGHJKLZXCVBNM MNBVCXZLKJHGFDSAPOIUYTREWQ ZYXWVUTSRQPONMLKJIHGFEDCBA
