import random
import validators
from pip._vendor import requests

maxVal = 99999


def randomMedia(base, mod):  # temp to see how long it takes...later
    while True:
        temp = base + mod + str(random.randint(1, maxVal))
        if validators.url(temp) and requests.get(temp).status_code != 404:
            return temp
