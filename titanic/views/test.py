from titanic.models.dataset import Dataset
from titanic.models.service import Service

class Test(object):

    dataset: object = Dataset()
    service: object = Service()

    def __init__(self, train):
        self.train = train
        service = self.service
        this = self.da



