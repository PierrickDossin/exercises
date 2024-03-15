# Write your code here

# Write your code here
import requests
import re


def one_or_more_b(string):
    return re.fullmatch(r'b+', string)