from bs4 import BeautifulSoup
import requests
import pandas as pd

class Melon(object):
    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dic = {}
    df = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).txt
    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')

    def ranking_to_dic(self):
        pass
    def dic_to_df(self):
        pass
    def df_to_csv(self):
        pass

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            m = input('0.exit 1.url 2.print 3.dic 4.dataframe 5.csv')
            if m == '0':
                break
            elif m == '1':
                melon.set_url()
            elif m == '2':
                melon.get_ranking()
            elif m == '3':
                melon.ranking_to_dic()
            elif m == '4':
                melon.dic_to_df()
            elif m == '5':
                melon.df_to_csv()
            else:
                continue
Melon.main()
