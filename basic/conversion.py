import pandas as pd

class Conversion(object):
    i = 0
    f = 0.0
    s = ''
    ls = []
    t = ()
    d = {}
    p = pd.DataFrame

    def create_tuple(self):
        self.t = (1,2,3,4,5,6,7,8,9,10)
        return self.t

    def t_to_l(self):
        self.create_tuple()
        self.ls = list(self.t)
        return self.ls

    def ls_to_f(self):
        self.t_to_l()
        self.ls = [float (i) for i in self.t]
        #self.t = list(map(float,self.t))
        return self.ls

    def f_to_i(self):
        self.ls_to_f()
        self.ls = [int (i) for i in self.t]
        #self.t = list(map(int,self.t))
        return self.ls

    def ls_to_dic(self):
        self.f_to_i()
        index = [0,1,2,3,4,5,6,7,8,9]
        index = [str (i) for i in index]
        self.d = dict(zip(index, self.ls))
        return self.d

    def str_to_t(self):
        self.s = 'hello'
        self.t = tuple(self.s)
        return self.t

    def t_to_l2(self):
        self.str_to_t()
        self.ls = list(self.t)
        return self.ls

    def dataframe(self):
        self.ls_to_dic()
        #self.d.update({'0':'number','1':'name','2':'address'})
        self.p = pd.Series(self.d)
        return self.p

#return은 저장하지 않고 쓰고 버리는 값(단순히 보여줄 때)

    @staticmethod
    def main():
        c = Conversion()
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list')
            if m == '0':
                break
            # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                print(c.create_tuple())
            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                print(c.t_to_l())
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                print(c.ls_to_f())
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                print(c.f_to_i())
            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                print(c.ls_to_dic())
            # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                print(c.str_to_t())
            # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                print(c.t_to_l2())
            # 5번 딕셔너리를 데이터프레임으로 전환하시오
            elif m == '8':
                print(c.dataframe())
            else:
                continue
Conversion.main()