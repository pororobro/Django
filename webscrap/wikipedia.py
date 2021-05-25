class Wikipedia(object):

    #url = ''

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    @staticmethod
    def main():

        while 1:
           # wiki = Wikipedia
            menu = input('0.Exit 1.Input URL 2.Print URL')
            if menu == '0' :
                break
            elif menu == '1':
                wiki = Wikipedia(input('Input URL'))
            elif menu == '2':
                print(wiki)
            else :
                print('Wrong number')
                continue

Wikipedia.main()
