from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver

class NaverMovie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = ''
    driver = webdriver.Chrome('C:/program Files/Google/Chrome/chromedriver')
    driver.implicitly_wait(3)
    df = None
    dt = {}
    ls = []
    ls1 = []
    ls2 = []
    ls3 = []

    def scrap(self):
        self.driver.get(self.url)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        ls_soup = soup.find_all('div', {'class':self.class_name})
        for i in ls_soup:
            self.ls1.append(i.find("a").text)
        for href in ls_soup:
            self.ls2.append(f' - https://movie.naver.com' + href.find("a")['href'])
        self.ls = [self.ls1, self.ls2]
        #self.ls = [ x + y for x, y in zip(self.ls1,self.ls2)]
        print(self.ls)

       # self.ls2 = list(range(1,51))
        for j in range(1,51):
            self.ls3.append(j)#(f'{j}위')
        print(self.ls3)

    def ls_to_dt(self):

        self.dt = dict(zip(self.ls3, self.ls))
        print(self.dt)

    def dt_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dt)#, orient='index', columns=['         TITLE         ','         LINK         '])
        self.df.rename(columns={0: '', 1: '           영화제목          ', 2: '          링크           ', 3: '런타임'}, inplace=True)
        print(self.df)

    def df_to_csv(self):
        path = './csv/naver_movie.csv'
        self.df.to_csv(path,sep='.', na_rep='-')

if __name__ == '__main__':
    nm = NaverMovie()
    nm.class_name = 'tit3'
    nm.scrap()
    nm.ls_to_dt()
    nm.dt_to_dataframe()
    nm.df_to_csv()