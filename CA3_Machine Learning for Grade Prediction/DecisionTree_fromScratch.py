import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature          
        self.threshold = threshold      
        self.left = left                
        self.right = right              
        self.value = value              

    def is_leaf_node(self):
        return self.value is not None


class DecisionTree:
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.root = None

    def fit(self, X, y):
        self.root = self._build_tree(X, y)

    def _build_tree(self, X, y, depth=0):
        num_samples, num_features = X.shape
        num_labels = len(set(y))

        
        if depth >= self.max_depth or num_labels == 1 or num_samples == 0:
            leaf_value = self._majority_vote(y)
            return Node(value=leaf_value)

        
        best_feature, best_thresh = self._best_split(X, y, num_features)
        if best_feature is None:
            return Node(value=self._majority_vote(y))

        
        left_idxs = X[:, best_feature] < best_thresh
        right_idxs = ~left_idxs
        left = self._build_tree(X[left_idxs], y[left_idxs], depth + 1)
        right = self._build_tree(X[right_idxs], y[right_idxs], depth + 1)
        return Node(best_feature, best_thresh, left, right)

    def _best_split(self, X, y, num_features):
        best_gain = -1
        best_feature, best_thresh = None, None
        for feature in range(num_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                gain = self._information_gain(y, X[:, feature], threshold)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_thresh = threshold
        return best_feature, best_thresh

    def _entropy(self, y):
        counts = np.bincount(y)
        probs = counts / len(y)
        return -np.sum([p * np.log2(p) for p in probs if p > 0])

    def _information_gain(self, y, feature_column, threshold):
        parent_entropy = self._entropy(y)
        left_idxs = feature_column < threshold
        right_idxs = ~left_idxs
        if len(y[left_idxs]) == 0 or len(y[right_idxs]) == 0:
            return 0
        n = len(y)
        n_left, n_right = len(y[left_idxs]), len(y[right_idxs])
        e_left = self._entropy(y[left_idxs])
        e_right = self._entropy(y[right_idxs])
        child_entropy = (n_left / n) * e_left + (n_right / n) * e_right
        return parent_entropy - child_entropy

    def _majority_vote(self, y):
        counter = Counter(y)
        return counter.most_common(1)[0][0]

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        if x[node.feature] < node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)
