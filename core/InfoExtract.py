from urllib.request import urlopen

from bs4 import BeautifulSoup


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
    title = allText[0]
    return allText[0].split("-")[0]
