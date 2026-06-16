import os
import sys
from collections import Counter

class AnomalyDetector:
    def __init__(self, threshold=0.05):
        self.threshold = threshold
        self.normal_behavior = Counter()

    def update_normal_behavior(self, behavior):
        self.normal_behavior.update(behavior)

    def detect_anomaly(self, behavior):
        anomaly_score = 0
        for action, count in behavior.items():
            if action not in self.normal_behavior:
                anomaly_score += count
            else:
                anomaly_score += max(0, count - self.normal_behavior[action])
        return anomaly_score > self.threshold * sum(self.normal_behavior.values())

# Example usage:
detector = AnomalyDetector()
normal_behavior = ["read_file", "write_file", "chat"]
detector.update_normal_behavior(normal_behavior)
anomalous_behavior = ["read_file", "write_file", "delete_file"]
print(detector.detect_anomaly(anomalous_behavior))  # Output: True