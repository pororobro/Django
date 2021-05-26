'''
구구단 프로그램은 단을 입력받아서, 입력받은 단의 1-9의 곱을 출력하는 어플이다.
단, 단은 정수이다.
'''

class Gugudan(object):

    dan = 0

    def multi(self):
        for i in range(1,10):
            print(f'{self.dan}*{i}={i*self.dan}')

    def multi2(self):
        for i in range(1,10):
            for dan in range(1,10):
                print(f'{dan}*{i}={i*dan}')

    @staticmethod
    def main():
        gugu = Gugudan()
        while 1:
            menu = int(input('0.exit 1.구구단 2.모든 단'))
            if menu == 0:
                break
            elif menu == 1:
                gugu.dan = int(input('단을 입력해주세요'))
                gugu.multi()
            elif menu == 2:
                gugu.dan = int(input('단을 입력해주세요'))
                gugu.multi2()
            else:
                continue

Gugudan.main()