import requests
from bs4 import BeautifulSoup


class Card:

    def __init__(self, string):
        self.url = "https://en.wikipedia.org/wiki/" + string
        self.title = None
        self.text = None
        self.image = None
        self._req = requests.get(self.url)
        self._soup = BeautifulSoup(self._req.content, 'html.parser')
        self.get_title()
        self.get_text()
        self.get_image()

    def get_title(self):
        self.title = (self._soup.find("h1", class_="firstHeading").string)


    def get_text(self):
        textcontainer = self._soup.find("div", class_="mw-parser-output")
        textcontainer = textcontainer.findChild("p")
        while len(textcontainer) < 10:
            textcontainer = textcontainer.findNext("p")
        textcontainer = textcontainer.get_text()
        self.text = textcontainer


    def get_image(self):
        images = (self._soup.find("a", class_="image").get("href"))
        large = requests.get("https://en.wikipedia.org//" + images)
        big_image = BeautifulSoup(large.content, 'html.parser')
        link = big_image.find("div", class_="fullImageLink")
        link = link.findChild("a").get("href")
        self.image= "https:" + link

