import pandas as pd
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KNNClassifier:
    def __init__(self):
        pass

    def load_csv(self, csv_path: str) -> Tuple[pd.DataFrame, pd.Series]:
        dataset = pd.read_csv(csv_path, delimiter=',', error_bad_lines=False)
        dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)
        x, y = dataset.iloc[:, :-1], dataset.iloc[:, -1]
        return x, y


    def train_test_split(self, features: pd.DataFrame, labels: pd.Series, test_split_ratio: float) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
        test_size = int(len(features) * test_split_ratio)
        train_size = len(features) - test_size
        x_train, y_train = features.iloc[:train_size, :], labels.iloc[:train_size]
        x_test, y_test = features.iloc[train_size:train_size + test_size, :], labels.iloc[train_size:train_size + test_size]
        return x_train, y_train, x_test, y_test

    def euclidean(self, points: pd.DataFrame, element_of_x: pd.Series) -> pd.Series:
        return ((points - element_of_x) ** 2).sum(axis=1).pow(0.5)

    def predict(self, x_train: pd.DataFrame, y_train: pd.Series, x_test: pd.DataFrame, k: int) -> pd.Series:
        labels_pred = []
        for _, x_test_element in x_test.iterrows():
            distances = self.euclidean(x_train, x_test_element)
            distances = pd.DataFrame({'distance': distances, 'label': y_train}).sort_values(by='distance')
            label_pred = mode(distances.head(k)['label']).mode[0]
            labels_pred.append(label_pred)
        return pd.Series(labels_pred, dtype=int)

    def accuracy(self, y_test: pd.Series, y_preds: pd.Series) -> float:
        true_positive = (y_test.reset_index(drop=True) == y_preds.reset_index(drop=True)).sum()
        return true_positive / len(y_test) * 100

    def plot_confusion_matrix(self, y_test: pd.Series, y_preds: pd.Series):
        conf_matrix = confusion_matrix(y_test, y_preds)
        sns.heatmap(conf_matrix, annot=True)

    def best_k(self, x_train, y_train, x_test, y_test, k_min=1, k_max=20):
        best_k_value, best_accuracy = 0, 0
        for k in range(k_min, k_max + 1):
            y_preds = self.predict(x_train, y_train, x_test, k)
            acc = self.accuracy(y_test, y_preds)
            if acc > best_accuracy:
                best_k_value, best_accuracy = k, acc
        return best_k_value, round(best_accuracy, 2)


csv_path = "HAZI/HAZI05/HAZI05.py"

knn = KNNClassifier()
x, y = knn.load_csv(csv_path)
x_train, y_train, x_test, y_test = knn.train_test_split(x, y, test_split_ratio=0.2)
y_preds = knn.predict(x_train, y_train, x_test, k=3)
acc = knn.accuracy(y_test, y_preds)
knn.plot_confusion_matrix(y_test, y_preds)
best_k_value, best_accuracy = knn.best_k(x_train, y_train, x_test, y_test)
print("Best k value:", best_k_value)
print("Best accuracy:", best_accuracy)
