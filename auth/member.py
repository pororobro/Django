class Member(object):

    id = ''
    name = ''
    email = ''
    pw = ''

    #회원가입(아이디,본명,이메일,비밀번호), 로그인, 마이페이지, 회원탈퇴

    def login(self):
        self.id = input('id')
        self.name = input('name')
        self.email = input('email')
        self.pw = input('pw')



    @staticmethod
    def main():
        member = Member()
        while 1 :
            menu = input('0.Exit 1.회원가입 2.로그인 3.마이페이지 4.회워탈퇴')
            if menu == '0':
                break
            elif menu == '1': #회원가입 (아이디, 본명, 이메일, 비밀번호)

                member.id = 'in'
            elif menu == '2':#아이디와 패스워드 받아서 비교해 같으면 로그인
                pass
            elif menu == '3 ': #회원가입 한 내용 출력 (비밀번호는 별 표시)
                pass
            elif menu == '4': #해당 리스트 삭제
                pass
            else:
                print('Wrong number')
                continue

Member.main()
