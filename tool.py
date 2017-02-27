import numpy as np

def sort(s):
   r=[]
   for i in range(len(s)):
      r.append((i+1,s[i]))
   r.sort(key=lambda tup:tup[1],reverse=True)
   r=np.asarray(r)
   return r