import numpy as np

def pair(x, y):
   x2 = []
   y2 = []
   
   for i in range(len(x)):
      for k in range(len(x)):
         if i==k or y[i,0]==y[k,0] or y[i,1]!=y[k,1]:
            continue
         x2.append(x[i]-x[k])
         y2.append(np.sign(y[i,0]-y[k,0]))
   
   return np.asarray(x2), np.asarray(y2)