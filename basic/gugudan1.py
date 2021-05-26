class Gugudan(object):
    dan = 0
    dic = {}

    def multi(self):
        for i in range(1,10):
            print(f'{i}*{self.dan}={i*self.dan}')

    def dic_dan(self):
        d = self.dic
        for i in range(1,10):
            d[i] = self.dan * i
        print('딕셔너리 출력')
        print(d)
        for j in d.keys():
            print(f'{self.dan}*{j}={d.get(j)}')


    @staticmethod
    def main():
        gugu = Gugudan()
        while 1:
            menu = input('0.exit 1.dan 2.all 3.dict ')
            if menu == '0':
                break
            elif menu == '1':
                gugu.dan = int(input('단을 입력해주세요'))
                gugu.multi()
            elif menu == '2':
                pass
            elif menu == '3':
                gugu.dan = int(input('단을 입력해주세요'))
                gugu.dic_dan()
            else:
                continue

Gugudan.main()