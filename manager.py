# Copyright 2022 by Néstor Nahuatlato
# <soy_nestor@hotmail.com>
# Licensed under GNU General Public License 3.0 or later.
# @license GPL-3.0+

from re import match
from os import system
from time import sleep
from constants import *

class Manager:
    def __init__(self):
        pass

    def guide(self):
        text = ""
        text += ">" * CHAR_REPETITIONS + "\n"
        text += "Type a number following any of these rules.\n\n"
        text += "DECIMAL: from 0 to 9\n"
        text += f"BINARY ({bin_prefix}): 0 and 1\n"
        text += f"OCTAL ({oct_prefix}): from 0 to 7\n"
        text += f"HEXADECIMAL ({hex_prefix}): from 0 to 9 and from 'a' to 'f'\n\n"
        text += f"Exit: '{EXIT}'\n"
        text += "<" * CHAR_REPETITIONS + "\n"
        return text

    def check(self, string, pattern, base):
        result = string.isdecimal() if pattern is None else match(pattern, string)
        return self.show_values(string=string, base=base) if result else NUMBER_ERROR

    def show_values(self, string, base):
        aux = int(string, base)
        return f"BIN {bin(aux)}\nOCT {oct(aux)}\nDEC {aux}\nHEX {hex(aux)}\n"

    def work(self):#The only function allowed to print in console
        while True:
            system(CLEAR)

            print(self.guide())
            string = input().lower()
            valid_input = True
            pattern, base = None, dec_base

            system(CLEAR)
            if string == EXIT:
                print(GOOD_BYE)
                break
            elif len(string) < C_1:
                valid_input = False
            else:
                user_prefix = string[C_0:C_2]

                if user_prefix == bin_prefix:
                    pattern, base = bin_pattern, bin_base
                elif user_prefix == oct_prefix:
                    pattern, base = oct_pattern, oct_base
                elif user_prefix == hex_prefix:
                    pattern, base = hex_pattern, hex_base
                else:
                    pass

            if valid_input:
                print(self.check(string=string, pattern=pattern, base=base))
            else:
                print(INPUT_ERROR)
                sleep(C_2)
