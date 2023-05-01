import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import sklearn.datasets as datasets


class KMeansOnDigits:
    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.digits = None
        self.clusters = None
        self.labels = None
        self.accuracy = None
        self.model = None

    def load_digits(self):
        self.digits = datasets.load_digits()

    def predict(self):
        self.model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.clusters = self.model.fit_predict(self.digits.data)
        return self.model, self.clusters

    def get_labels(self):
        labels = np.zeros_like(self.clusters)
        for i in range(10):
            mask = (self.clusters == i)
            labels[mask] = mode(self.digits.target[mask])[0]
        self.labels = labels
        return labels

    def calc_accuracy(self, target_labels:np.ndarray,predicted_labels:np.ndarray):
        self.accuracy = accuracy_score(target_labels, predicted_labels)
        return round(self.accuracy, 2)

kmeans_model = KMeansOnDigits(n_clusters = 10, random_state = 0)

kmeans_model.load_digits()
kmeans_model.predict()
kmeans_model.get_labels()
kmeans_model.calc_accuracy(kmeans_model.digits.target, kmeans_model.labels)