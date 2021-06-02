import pandas as pd
from titanic.models.dataset import Dataset
from titanic.models.service import Service

class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(test)
        this.train = service.create_train()

        return this

    def learning(self, train, test):
        this = self.modeling(self,train, test)
        print(f'사이킷런의 SVC 알고리즘 정확도 {self.service.accuracy_by_svm(this)}%')

    def preprocess(self, train, test) -> object: #전처리 본격적으로 하기전에 데이터를 다듬음
        service = self.service
        this = self.dataset
        #초기 모델 생성
        this.train = service.new_model(train)
        this.test = service.new_model(test)

        # norminal, ordinal 로 정형화
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)

        this = service.gender_norminal(this)
        this = service.age_ordinal(this)
#        this = service.fare_band_fill_na(this)

        #this = service.fare_ordinal(this)

        # 불필요한 feature(name) 제거
        this = service.drop_feature(this, 'Cabin','Ticket', 'Name', 'Sex')

        self.print_this(this)

        return this

    @staticmethod
    def print_this(this):

        print('*'*100)
        print(f'1. Train 의 type 은\n{type(this.train)}이다')
        print(f'2. Train 의 column 은\n{this.train.columns}이다')
        print(f'3. Train 의 상위 5개 행은\n{this.train.head(5)}이다')
        print(f'4. Train 의 null 의 갯수\n{this.train.isnull().sum()}개')
        print(f'5. Test 의 type 은\n {type(this.test)}이다')
        print(f'6. Test 의 column 은\n {this.test.columns}이다')
        print(f'7. Test 의 상위 5개 행은\n {this.test.head(5)}이다')
        print(f'8. Test 의 null 의 갯수\n {this.test.isnull().sum()}개')
        print('*'*100)
