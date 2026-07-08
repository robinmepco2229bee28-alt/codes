import re

# Range: 100000 - 999999 (6 digits, first digit not 0)
regex_integer_in_range = r"^[1-9]\d{5}$"

# Alternating repetitive digits: (digit)(any_digit)(same_digit)
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
