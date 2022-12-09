# Copyright 2022 by Néstor Nahuatlato
# <soy_nestor@hotmail.com>
# Licensed under GNU General Public License 3.0 or later.
# @license GPL-3.0+

from os import name

# Numeric systems patterns
bin_pattern = '0b[0,1]'
oct_pattern = '0o[0-7]'
hex_pattern = '0x[0-9,a-f]'

# Binary, Octal and Hexadecimal prefixes
bin_prefix = '0b'
oct_prefix = '0o'
hex_prefix = '0x'

#Numeric systems bases
bin_base = 2
oct_base = 8
dec_base = 10
hex_base = 16

# Auxliriary constants
C_0 = 0
C_1 = 1
C_2 = 2
CHAR_REPETITIONS = 20
NUMBER_ERROR = "You've typed an invalid number"
INPUT_ERROR = "Wrong input... Try again! =)"
GOOD_BYE = "Bytes!"
EXIT = 'e'
CLEAR = "cls" if name == 'nt' else "clear"