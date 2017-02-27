import numpy as np
from tool import sort
from sklearn.metrics.pairwise import cosine_similarity

def baseline(x,x2):
   s=[]
   for i in range(len(x)):
      
      c=0
      for t in x2:
         c+=cosine_similarity(x[i].reshape(1,-1),t.reshape(1,-1))[0,0]
      s.append(c)
      
   return sort(np.asarray(s,'f'))