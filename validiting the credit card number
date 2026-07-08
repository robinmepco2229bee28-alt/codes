# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def validate_card(card_number):
    # Rule 1-4: Check starting digit, overall length, digit content, and grouping
    # ^[456]             : Starts with 4, 5, or 6
    # (                  : Start of group
    #   \d{15}           : Exactly 15 more digits (total 16)
    #   |                : OR
    #   \d{3}(-\d{4}){3} : 3 digits, then 3 groups of (- followed by 4 digits)
    # )                  : End of group
    # $                  : End of string
    structure_regex = r"^[456](\d{15}|\d{3}(-\d{4}){3})$"
    
    if not re.match(structure_regex, card_number):
        return "Invalid"
    
    # Rule 5: Check for 4 or more consecutive repeated digits
    # First, strip hyphens to check the raw sequence of digits
    clean_number = card_number.replace("-", "")
    
    # (\d)               : Match any digit and capture it
    # \1{3,}             : Match the same digit 3 or more additional times
    if re.search(r"(\d)\1{3,}", clean_number):
        return "Invalid"
        
    return "Valid"

# Processing Input
try:
    n = int(input().strip())
    for _ in range(n):
        print(validate_card(input().strip()))
except EOFError:
    pass
