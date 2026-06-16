import os
import json
from collections import deque

class AnomalyDetector:
    def __init__(self):
        self.anomaly_threshold = 0.5
        self.recent_activity = deque(maxlen=10)

    def detect_anomaly(self, activity):
        # Calculate the anomaly score based on recent activity
        anomaly_score = self.calculate_anomaly_score(activity)
        if anomaly_score > self.anomaly_threshold:
            return True
        return False

    def calculate_anomaly_score(self, activity):
        # Implement a machine learning model to calculate the anomaly score
        # For simplicity, a basic calculation is used here
        return sum([1 for a in self.recent_activity if a != activity]) / len(self.recent_activity)

    def update_recent_activity(self, activity):
        self.recent_activity.append(activity)