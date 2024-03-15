# Write your code here
import requests
import re


def only_digits(string):
    return re.fullmatch(r'(0|1|2|3|4|5|6|7|8|9)*', string)