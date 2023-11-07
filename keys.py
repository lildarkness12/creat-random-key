import string
import random

STR = string.ascii_letters
KEY = "".join(random.sample(STR, 30))
num = (random.randint(10000, 99999))

print(KEY + str(num))
