# Write your code here
import requests
import re


def two_or_more_abc(string):
    return re.search(r'(abc){2,}', string)