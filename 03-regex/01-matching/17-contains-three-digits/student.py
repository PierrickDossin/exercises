# write your code here

import re

def contains_three_digits(string):
    digit_count = re.findall(r'\d', string)
    return len(digit_count) >= 3