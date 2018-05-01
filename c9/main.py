import numpy as np
import scipy.misc as mc
import scipy.optimize as opt
import scipy
import sys
photo=mc.imread(sys.argv[1])

tiras=np.array([photo[:,i,:].ravel() for i in range(photo.shape[1])],
        dtype=float)
distances_matrix=scipy.spatial.distance.cdist(tiras,tiras,'correlation')
distances_matrix+=np.eye(distances_matrix.shape[0])*9999999999999999

##rows,cols=opt.linear_sum_assignment(distances_matrix)
#
r=0
s=[0]
print('>------------>')
S=set()
for I in range(distances_matrix.shape[0]):
    rs=np.argsort(distances_matrix[r]    )
    i=0
    while rs[i] in S:
        i+=1
    S.add(rs[i])
    if i==len(rs):
        break
    r=rs[i]
    s.append(r)
mc.imshow(photo[:,s,:])
#def align(tiras):
#    for i in tiras:
#        while 
#KKtWDErYcZbyfWvCpXDV
