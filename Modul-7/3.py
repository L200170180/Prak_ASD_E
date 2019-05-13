import re

wiki = open("Indonesia.txt", "r")
teks = wiki.read()
wiki.close()

print(re.findall(r'di \w+', teks.lower()))
