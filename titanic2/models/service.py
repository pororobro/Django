import pandas as pd
from titanic.models.dataset import Dataset
import numpy as np

class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this,*feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
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
    def fare_ordinal(this) -> object:
        this.test
        for i in this.train, this.test:
            i['AgeGroup'] = pd.qcut(i['Fare'],4,{4,3,2,1})
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

        '''
        train = this.train
        test = this.test

        for i in train, test:
            i['Age'] = i.fillna(-0.5)

        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        #train['AgeGroup'] = pd.cut(train['Age'],bins= bins, labels=labels)
        #test['AgeGroup'] = pd.cut(test['Age'],bins=bins, labels=labels)
        ge_title_mapping = {'Unknown':0, 'Baby':1, 'Child':2, 'Teenager':3, 'Student':4, 'Young Adult':5,
                            'Adult':6, 'Senior':7}

        for i in train, test:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(ge_title_mapping)

        #this.train = this.train.fillna({'Age': 0})
        #this.test = this.test.fillna({'Age': 0})
        #'Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior'
        return this
'''
    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # np.inf - 주어진 범위 그 이후 값 통합, -1: (미상에 대한 처리)
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5,
                             'Adult': 6, 'Senior': 7}
        for dataset in train, test:
            dataset['AgeGroup'] = pd.cut(dataset['Age'], bins=bins, labels=labels)  # key, value 이름이 같으면 key 생략가능
            dataset['AgeGroup'] = dataset['AgeGroup'].map(age_title_mapping)

        return this
        #fare_band_norminal