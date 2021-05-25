from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):

    url = ''

    def __str__(self): #이 안에 들어있는
        return self.url


    def scrap(self, class_name):

        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        count = 0
        print("< ARTIST >")
        for link1 in soup.find_all(name='p', attrs=({"class": class_name[0] })):
            count += 1
            print(f'순위: {str(count)} ')
            print( f'{class_name[0]}: {link1.find("a").text}')
        print("< TITLE >")
        for link1 in soup.find_all(name='p', attrs=({"class": class_name[1] })):
            count += 1
            print(f'순위: {str(count)} ')
            print(f'{class_name[1]}: {link1.find("a").text}')

    #https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210524&charthour=15
    @staticmethod
    def main():

        bugs = BugsMusic()
        while 1:
            menu = int(input('0.Exit\n1.Input URL\n2.Get Ranking'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input URL')
            elif menu == 2:
                bugs.scrap(["artist","title"])
            else:
                print('Wrong number')
                continue



BugsMusic.main()