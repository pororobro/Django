import pandas as pd

class Conversion(object):

    @staticmethod
    def create_tuple() -> ():
       # self.t = (1,2,3,4,5,6,7,8,9,10)
       # return self.t
        return (1,2,3,4,5,6,7,8,9,10)

    @staticmethod
    def t_to_l(t) -> []:
        return list(t)

    @staticmethod
    def i_to_f(ls) -> []:
        return [float (i) for i in ls]


    @staticmethod
    def f_to_i(ls) -> []:
        return [int (i) for i in ls]

    @staticmethod
    def ls_to_dic(ls) -> {}:
        index = [0,1,2,3,4,5,6,7,8,9]
        index = [str (i) for i in index]
        return dict(zip(index, ls))

    @staticmethod
    def str_to_t() -> ():
        #s = 'hello'
        #t = tuple(s)
        #return t
        return tuple('hello')

    @staticmethod
    def t_to_l2(t) -> []:
        return list(t)

    @staticmethod
    def dataframe(d) -> object:

        #self.d.update({'0':'number','1':'name','2':'address'})
        return pd.Series(d)

#return은 저장하지 않고 쓰고 버리는 값(단순히 보여줄 때)

    @staticmethod

    def main():
        c = Conversion()
        i = 0
        f = 0.0
        s = ''
        ls = []
        t = ()
        d = {}
        p = pd.DataFrame

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
                t = c.create_tuple()
                print(t)
            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                ls = c.t_to_l(t)
                print(ls)
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                ls = c.i_to_f(ls)
                print(ls)
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                ls = c.f_to_i(ls)
                print(ls)
            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                d = c.ls_to_dic(ls)
                print(d)
            # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                t = c.str_to_t()
                print(t)
            # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                ls = c.t_to_l2(t)
                print(ls)
            # 5번 딕셔너리를 데이터프레임으로 전환하시오
            elif m == '8':
                p = c.dataframe(d)
                print(p)
            else:
                continue
Conversion.main()