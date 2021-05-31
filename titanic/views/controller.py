import pandas as pd
from titanic.models.dataset import Dataset
from titanic.models.service import Service

class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:

        service = self.service
        this = self.preprocss(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocss(self, train, test) -> object: #전처리 본격적으로 하기전에 데이터를 다듬음
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'Train의 type은 {type(this.train)}이다')
        print(f'Train의 column은 {this.train.columns}이다')
        print(f'Train의 상위 5개 데이터는 {this.train.head()}이다')
        print(f'Train의 하위 5개 데이터는 {this.train.tail()}이다')
        return this
