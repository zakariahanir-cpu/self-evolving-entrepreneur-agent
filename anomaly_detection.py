import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

class AnomalyDetector:
    def __init__(self, data):
        self.data = data
        self.model = IsolationForest()

    def train(self):
        self.model.fit(self.data)

    def predict(self, new_data):
        return self.model.predict(new_data)