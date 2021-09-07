import random
import validators
from pip._vendor import requests

maxVal = 99999


def randomMedia(base, mod):  # temp to see how long it takes...later
    print("Searching...")
    while True:
        temp = base + mod + str(random.randint(1, maxVal))
        if validators.url(temp) and requests.get(temp).status_code != 404:
            print("Found!")
            return temp
