import pandas as pd
from titanic.models.dataset import Dataset

class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop(['Survived'], axis=1)

    @staticmethod
    def create_label(this) -> object:
        pass
        #return this.train['Survived']


    @staticmethod
    def drop_feature(this,feature) -> object:
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        print(f'타입체크 {this.train["Embarked"]}')
        #this.train.map({'S':1, 'Q':2,})
        embarked_mapping = {'S':1, 'C':2, 'Q':3}
        this.train['Embarked'] = this.train['Embarked'].map(embarked_mapping)
        this.test['Embarked'] = this.test['Embarked'].map(embarked_mapping)
        #map(this.train, [this.train[i]for i in this.train])
        #map(this.test, [this.test[i] for i in this.test])
        #map 함수를 사용하며 S: 1, C: 2, Q: 3

        return this

    @staticmethod
    def fare_band_fill_na(this) -> object:
        return this

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.',expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            #this.train = this.train.fillna({'Title': 0})
            #this.test = this.test.fillna({'Title': 0})
            #this.train['Title'] = this.train['Title'].map(title_mapping)
            #this.test['Title'] = this.test['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
            #fillna(0) - 0은 호칭이 없는 극빈, 노예
        return this

    @staticmethod
    def gender_norminal(this) -> object:
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].fillna(0)
            dataset['Gender'] = dataset['Sex'].map(gender_mapping)
        this.train = combine[0]
        this.train = combine[1]
        return this





    #fare_band_norminal