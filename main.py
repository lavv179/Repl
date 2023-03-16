# Sample input string
import re

def extract_hex_color_codes(input_str):
    hex_color_regex = r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b'
    hex_color_codes = re.findall(hex_color_regex, input_str)
    return hex_color_codes

input_str = "#123456 #789 #abcDEF #666ZZZ"
hex_color_codes = extract_hex_color_codes(input_str)
print(hex_color_codes)
