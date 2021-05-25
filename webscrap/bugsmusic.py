from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):

    url = ''

    def __str__(self): #이 안에 들어있는
        return self.url

    @staticmethod
    def rank(something):
        bugs = BugsMusic()
        soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
        count = 0
        for link1 in soup.find_all(name='p', attrs=({"class": something })):
            count += 1
            print(f'순위: {str(count)} ')
            print( f'{something}: {link1.find("a").text}')

    #https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210524&charthour=15
    @staticmethod
    def main():


        while 1:
            menu = int(input('0.Exit\n1.Input URL\n2.Print URL'))
            if menu == 0:
                break
            elif menu == 1:
                BugsMusic.url = input('Input URL')
            elif menu == 2:
                print(f':입력된 URL :::::::::::::::::::: {BugsMusic.url}')

                print('------------------------- ARTIST RANKING ---------------------------')
                BugsMusic.rank("artist")

                print('------------------------- TITLE RANKING ---------------------------')
                BugsMusic.rank("title")

            else:
                print('Wrong number')
                continue



BugsMusic.main()