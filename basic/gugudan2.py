class Gugudan(object):
    dan = 0
    dic = {}

    def multi(self):
        for i in range(1,10):
            print(f'{self.dan}*{i}={self.dan*1}')

    def dict(self):

        for i in range(1,10):
            self.dic[i] = self.dan * i
        print(self.dic)
        for k in self.dic.keys():
            print(f'{self.dan}*{k} = {self.dic.get(k)}')

    @staticmethod
    def main():
        gugu = Gugudan()
        while 1:
            menu = input('0.exit 1.dan 2.dic')
            if menu == '0':
                break
            elif menu == '1': #단 하나 입력 - > 그 단의 1-9까지 곱
                gugu.dan = int(input('단 입력'))
                gugu.multi()
            elif menu == '2': #단 하나 입력 - > 딕션너리 구조에 넣어서 1과 같은 출력
                gugu.dan = int(input('단 입력'))
                gugu.dict()
            else :
                continue
Gugudan.main()