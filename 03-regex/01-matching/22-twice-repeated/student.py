# Write your code here
import re

def twice_repeated(string):
    return re.search(r'^(.+)\1$', string)
