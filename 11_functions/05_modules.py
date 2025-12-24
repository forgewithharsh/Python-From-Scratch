# Two types of modules in python:
# - Built in Modules
# - External Modules

import math
import my_module
import requests

print(math.sqrt((16)))
my_module.hello()
r = requests.get("https://www.google.com")
print(r.text)