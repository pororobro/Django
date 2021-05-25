from bs4 import BeautifulSoup

class Bugs2(object):

    url = ''
    hdr =
    class_name = []

    def sef_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_ranking(self):
        bs = BeautifulSoup(self.url, 'html.parser')
        ls = bs.find_all(name='div', attrs=({'class':'ellipsis rank01'})

    @staticmethod
    def main():
        b = Bugs2()
        while 1:
            menu = input('0.Exit 1.URL')
            if menu == 0:
                break
            elif menu == 1:
                b.set_url(input('url'))
            elif menu == 2:
                b.get_ranking()
