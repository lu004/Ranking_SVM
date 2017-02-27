ランキング機会学習利用して最適のオブジェクト推薦
ranking SVM (python)
# task:
to recommend a item x
from a set of items {x}

# item x: ("x.csv")
x has feature values
a label of grade-level y

# grade-level y: ("y.csv")
y consists of grade (the first) and query id (the second)

# items are compared if items are in the same query id

# train data: all x,y
# test data: the first "k" persons (please read "x.csv" for knowing k's value)

# ranking SVM is implemented based on "pair-wise" approach
# this example is implemented by using machine learning tool "scikit-learn"
# (optional) pca for reducing feature dimension
# (optional) baseline method for this task:
finding most simimlar items (in test data) with items of high grade (in the train data)
