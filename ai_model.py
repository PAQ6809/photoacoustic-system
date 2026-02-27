"""
Prototype script for classifying photoacoustic signals using machine learning.

This module outlines a workflow for loading labelled feature data from a CSV
file, splitting the data into training and testing sets, training a simple
classifier, and evaluating its performance. It uses scikit‑learn for the
classification algorithm and assumes that the CSV file contains feature
vectors with the class label in the last column.

Note: scikit‑learn is not included in this repository. To run this script,
install it via pip (e.g. `pip install scikit-learn`). This script serves as a
reference for researchers wishing to experiment with machine learning on
photoacoustic data.
"""

from typing import Tuple, List

import csv


def load_dataset(file_path: str) -> Tuple[List[List[float]], List[int]]:
    """Load feature vectors and labels from a CSV file.

    The CSV is expected to have one sample per row, with the label in the
    last column and numeric features in all preceding columns.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A tuple (features, labels) where features is a list of lists of floats
        and labels is a list of integers.
    """
    features: List[List[float]] = []
    labels: List[int] = []
    with open(file_path, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            *feature_values, label_str = row
            try:
                feature_vector = [float(v) for v in feature_values]
                label = int(label_str)
            except ValueError:
                # Skip rows with non‑numeric data
                continue
            features.append(feature_vector)
            labels.append(label)
    return features, labels


def split_dataset(
    features: List[List[float]], labels: List[int], test_ratio: float = 0.2
) -> Tuple[List[List[float]], List[List[float]], List[int], List[int]]:
    """Split the dataset into training and testing sets.

    Args:
        features: List of feature vectors.
        labels: List of labels corresponding to the feature vectors.
        test_ratio: Proportion of the dataset to include in the test split.

    Returns:
        X_train, X_test, y_train, y_test
    """
    total = len(features)
    test_size = int(total * test_ratio)
    X_train = features[:-test_size] if test_size > 0 else features
    X_test = features[-test_size:] if test_size > 0 else []
    y_train = labels[:-test_size] if test_size > 0 else labels
    y_test = labels[-test_size:] if test_size > 0 else []
    return X_train, X_test, y_train, y_test


def train_knn_classifier(X_train: List[List[float]], y_train: List[int]):
    """Train a k‑nearest neighbours classifier using scikit‑learn.

    Args:
        X_train: Training feature vectors.
        y_train: Training labels.

    Returns:
        A trained KNeighborsClassifier instance.
    """
    try:
        from sklearn.neighbors import KNeighborsClassifier
    except ImportError as e:
        raise ImportError(
            "scikit‑learn is required for this function. Install it via pip before running."
        ) from e
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test: List[List[float]], y_test: List[int]) -> float:
    """Evaluate the classifier on the test set and return accuracy.

    Args:
        model: Trained classifier with a predict method.
        X_test: Test feature vectors.
        y_test: True labels for the test set.

    Returns:
        Classification accuracy as a float between 0 and 1.
    """
    if not X_test:
        return 0.0
    predictions = model.predict(X_test)
    correct = sum(int(p == y) for p, y in zip(predictions, y_test))
    return correct / len(y_test)


def main() -> None:
    """Example workflow using the helper functions.

    Replace 'pa_features.csv' with your own dataset file. Each row should
    contain numeric features followed by an integer label. For example:

        0.12,0.34,0.56,1
        0.22,0.44,0.66,0

    """
    features, labels = load_dataset("pa_features.csv")
    X_train, X_test, y_train, y_test = split_dataset(features, labels)
    model = train_knn_classifier(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Model accuracy: {accuracy:.2%}")


if __name__ == "__main__":
    main()
