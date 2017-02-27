from sklearn import svm
from pair import pair

def r_train(x,y):

   x2,y2=pair(x,y)
   svc=svm.SVC(kernel='linear').fit(x2,y2)

   return svc