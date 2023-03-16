import re

# Sample input string
input_str = "This is a sample input string with #FF0000 and #00FF00 hex color codes"

# Regular expression to match hex color codes
hex_regex = r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})"

# Find all hex color codes in the input string
hex_codes = re.findall(hex_regex, input_str)

# Print the hex color codes
print(hex_codes)



r"#([data]{time})|other regex"


r"value_search([variable_value]{repetitions})|other_condition\b"

\b = limit/strict search
