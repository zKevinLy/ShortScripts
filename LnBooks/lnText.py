
import requests
import re
import io
import os
from itertools import groupby
from bs4 import BeautifulSoup
from pathlib import Path


class Book:
    def __init__(self,title,startChapter,endChapter):
        self.title = title
        self.chapters = range(startChapter,endChapter+1)
        self.url = "https://readlightnovels.net"
        self.contentBlockName = "chapter-content"

    def createBook(self): 
        try:
            directory = Path(__file__).absolute().parent
            if 'Books' not in os.listdir(directory):
                os.mkdir('Books')
            with io.open(f"Books/{self.title.upper()}.txt",'w', encoding="utf-8") as book:
                pass
            for c in self.chapters:
                print(c)
                with io.open(f"Books/{self.title.upper()}.txt",'a', encoding="utf-8") as book:
                    book.write(f"\nChapter-{c}\n")
                    title = '-'.join(self.title.lower().split())
                    page = requests.get(f'{self.url}/{title}/chapter-{c}.html')
                    soup = BeautifulSoup(page.text, 'html.parser')
                    results = soup.findAll("div", {"class": self.contentBlockName})
                    for para in results:
                        s = re.sub(r'<[a-z]*>', '', para.text)
                        s = re.sub(r'</[a-z]*>', '', s)
                        s = re.sub(r'</[a-z]*[1-9]*>', '', s)
                        s = re.sub(r'<[a-z]*(\s)*/>', '', s)
                        book.write("{}\n".format(s))
        except:
            return 'Invalid title'

    def reformat(self):
        with io.open(f"Books/{self.title.upper()}.txt",'r+', encoding="utf-8") as book:
            lines = book.readlines()
            s = [l for l in lines if "You are reading on" not in l]
            s = [l for l in lines if "If you’re not reading this on" not in l]
            s = [x[0] for x in groupby(s)]
        with io.open(f"Books/{self.title.upper()}.txt",'w', encoding="utf-8") as book:
            [book.write(l) for l in s]
        


if __name__ == '__main__':
    orv = Book("THE BEGINNING AFTER THE END", 1, 500)
    orv.createBook()
    orv.reformat()
