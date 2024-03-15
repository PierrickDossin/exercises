# Write your code here
import re

def is_number(string):
    return re.search(r'^\d+(\.\d+)?$', string)