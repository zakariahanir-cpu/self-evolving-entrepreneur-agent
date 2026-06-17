import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.metrics import accuracy_score

class NLP:
    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

    def classify_text(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits
        return torch.argmax(logits)

    def evaluate(self, texts, labels):
        predictions = [self.classify_text(text) for text in texts]
        return accuracy_score(labels, predictions)