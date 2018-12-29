# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import scftypes
from pygra import operators
from scipy.sparse import csc_matrix
g = geometry.honeycomb_lattice()
g.write()
Us = np.linspace(0.,4.,10) # different Us
f = open("EVOLUTION.OUT","w") # file with the results
for U in Us: # loop over Us
  
  h = g.get_hamiltonian() # create hamiltonian of the system
  mf = scftypes.guess(h,mode="antiferro") # antiferro initialization
  # perform SCF with specialized routine for Hubbard
  scf = scftypes.hubbardscf(h,nkp=20,filling=0.5,g=U,
                mix=0.9,mf=mf)
  # alternatively use
#  scf = scftypes.selfconsistency(h,nkp=20,filling=0.5,g=U,
#                mix=0.9,mf=mf)
  h = scf.hamiltonian # get the Hamiltonian
  gap = h.get_gap() # compute the gap
  f.write(str(U)+"   "+str(gap)+"\n")
  
f.close()
