import spyder_kernels.customize.utils


class VectorTest(object):
    ls = ['abcd',786,2.23,'john',70.2]
    tinyls = [123,'john']
    tp = ('abcd',786,2.23,'john',70.2)
    tinytp = (123, 'john')
    dt = {'abcd':786,'john':70.2}
    tinydt = {'john':123}

    def ls_create(self):
        self.ls.append(100)
        print(self.ls)
    def ls_read(self):
        print(self.ls)
    def ls_merge(self):
        #self.ls = self.ls + self.tinyls
        #return
        self.ls.extend(self.tinyls)
        print(self.ls)
    def ls_delete(self):
        self.ls.remove(786)
        print(self.ls)

    def tp_create(self):
        self.tp = self.tp + (100, )
        print(self.tp)

    def tp_read(self):
        print(self.tp)

    def tp_merge(self):
        self.tp = self.tp + self.tinytp
        return print(self.tp)

    def tp_delete(self):
        print('Impossible')

    def dt_create(self):
        self.dt['tom'] = 100
        print(self.dt)

    def dt_read(self):
        print(self.dt)

    def dt_merge(self):
        self.dt.update(self.tinydt)
        print(self.dt)

    def dt_delete(self):
        del self.dt['abcd']
        print(self.dt())




    @staticmethod
    def main():
        v = VectorTest()
        while 1:
            menu = input('0. Exit\n'
                         'LIST : 1.Read,2.Create,3.Update,4.Delete\n'
                         'Tuple : 5.Read,6.Create,7.Update,8.Delete\n'
                         'Dictionary : 9.Read,10.Create,11.Update,12.Delete')
            if menu == '0':
                break
            elif menu == '1':
                v.ls_read()
            elif menu == '2':
                v.ls_create()
            elif menu == '3':
                v.ls_merge()
            elif menu == '4':
                v.ls_delete()
            elif menu == '5':
                v.tp_read()
            elif menu == '6':
                v.tp_create()
            elif menu == '7':
                v.tp_merge()
            elif menu == '8':
                v.tp_delete()
            elif menu == '9':
                v.dt_read()
            elif menu == '10':
                v.dt_create()
            elif menu == '11':
                v.dt_merge()
            elif menu == '12':
                v.dt_delete()
            else:
                continue

VectorTest.main()
