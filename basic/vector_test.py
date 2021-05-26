class VectorTest(object):
    ls = ['abcd',786,2.23,'john',70.2]
    tinyls = [123,'john']
    tp = ('abcd',786,2.23,'john',70.2)
    tinytp = (123, 'john')
    dt = {'abcd', 786, 2.23, 'john', 70.2}
    tinydt = {123, 'john'}

    def ls_create(self):
        self.ls.append(100)
    def ls_read(self):
        print(self.ls())
    def ls_merge(self):
        self.ls = self.ls + self.tinyls
        return
    def ls_delete(self):
        self.ls.remove()
    def tp_create(self):
        self.tp = self.tp + (100, )
        return
    def tp_read(self):
        print(self.tp())
    def tp_merge(self):

        return self.tp
    def tp_delete(self):
        self.ls = self.tp

    def dt_create(self):
        pass
    def dt_read(self):
        pass
    def dt_merge(self):
        pass
    def dt_delete(self):
        pass




    @staticmethod
    def main():
        vt = VectorTest()
        while 1:
            menu = input('0.exit 1.ls 2.tp 3.dt')
            if menu == '0':
                break
            elif menu == '1':
                print(vt.ls_create())

            else:
                continue

VectorTest.main()
