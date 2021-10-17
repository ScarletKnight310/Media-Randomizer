from urllib.request import urlopen

from bs4 import BeautifulSoup
lim = 100

def extractImage(url):
    url += "1"
    return url


def extractText(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.decompose()
    strips = list(soup.stripped_strings)
    return strips


def extractTitle(url):
    allText = extractText(url)
    return allText[0].split("-")[0]


def extractDesc(url):
    allText = extractText(url)
    desc = ""
    switch = False
    for line in allText:
        if switch and line == "[Written by MAL Rewrite]":
            switch = False
        if switch:
            desc += line
        if line == "Synopsis":
            switch = True
    cleanedDesc = desc.split("Synopsis")[1]
    result = []
    for i in range(0, len(cleanedDesc), lim):
        result.append(cleanedDesc[i: i + lim])
    finalDesc = ""
    for line in result:
        finalDesc += line + "\n"
    return finalDesc
