# Write your code here
# Write your code here
import requests
import re


def one_or_more_abc(string):
    return re.fullmatch(r'(abc)+', string)