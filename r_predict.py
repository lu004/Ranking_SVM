import numpy as np
from tool import sort

def r_predict(svc,x):
   
   s=[]
   for i in range(len(x)):
      t=[]
      for k in range(len(x)):
         if i!=k:
            t.append(x[i]-x[k])
      s.append(sum(svc.predict(np.asarray(t))))
   
   return sort(np.asarray(s))