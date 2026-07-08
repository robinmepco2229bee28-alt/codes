import re

# Read dimensions
n, m = map(int, input().split())

# Read matrix rows
matrix = [input() for _ in range(n)]

# Decode by columns: Join characters from top-to-bottom for each column
decoded_string = "".join([matrix[row][col] for col in range(m) for row in range(n)])

# Regex to replace non-alphanumeric characters between alphanumeric ones
# Pattern explanation: 
# (?<=[a-zA-Z0-9]) : Positive lookbehind for alphanumeric
# [^a-zA-Z0-9]+    : One or more non-alphanumeric characters
# (?=[a-zA-Z0-9])  : Positive lookahead for alphanumeric
pattern = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'

print(re.sub(pattern, ' ', decoded_string))
