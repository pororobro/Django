from bs4 import BeautifulSoup
import requests

class Melon(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []


    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text



    def get_ranking(self):
        count = 0
        soup = BeautifulSoup(self.url, 'lxml')
        print('-----------------제목-----------------')
        ls = soup.find_all('div', {'class': self.class_name[0]})
        for i in ls:
            count += 1
            print(f'순위: {str(count)} ')
            print(f' {i.find("a").text}')



    @staticmethod
    def main():
        m = Melon()
        while 1:
            menu = input('0.Exit 1.URL 2.Get Ranking 3.')
            if menu == '0':
                break
            elif menu == '1':
                m.set_url(input('날짜'))
            elif menu == '2':
                m.class_name.append('ellipsis rank01')
                m.class_name.append('ellipsis rank02')
                m.get_ranking()
            else:
                continue

Melon.main()
