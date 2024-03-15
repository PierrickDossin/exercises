# Write your code here
import re

def thrice_repeated(string):
    return re.search(r'^(.+)\1\1$', string)
