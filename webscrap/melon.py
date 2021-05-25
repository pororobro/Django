from bs4 import BeautifulSoup
from urllib.request import urlopen
class Melon(object):

    url = ''

    def __str__(self):
        return self.url

    def scrap(self, class_name):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = int(input('0.Exit 1.Input URL 2.Get Ranking'))
            if menu == 0:
                break
            elif menu == 1:
                melon.url = input('Input URL')
            elif menu == 2:
                print(melon.url)
            else:
                pass

Melon.main()