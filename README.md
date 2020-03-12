# Ranking SVM

Rank each item by "pair-wise" approach

## Implementation
- item x: ("x.csv") x has feature values and a grade-level y (at the same row in "y.csv")
- grade-level y: ("y.csv") y consists of grade (the first) and query id (the second)
- one x or one y is one row in "csv" file
- ranking SVM is implemented based on "pair-wise" approach
- items are compared if items are in the same query id
- this is implemented by using machine learning tool "scikit-learn"
- (optional) pca for reducing feature dimension
- (optional) baseline method for this task: finding most simimlar items (in test data) with items of high grade (in the train data)
- train/test data: please refer to "main.py"
