from ..superconductivity import get_eh_sector
from ..superconductivity import build_nambu_matrix
from ..multihopping import MultiHopping

def extract_anomalous_dict(dd):
    """Given a dictionary, extract the anomalous part"""
    out = dict()
    for key in dd:
        d = dd[key] # get this patrix
        m01 = get_eh_sector(d,i=0,j=1)
        m10 = get_eh_sector(d,i=1,j=0)
        m = build_nambu_matrix(m01*0.0,c12=m01,c21=m10) # build matrix
        out[key] = m
    return out # return dictionary




def get_anomalous_hamiltonian(self):
  """Turn a Hamiltonian into a Nambu Hamiltonian"""
  self = self.copy() # copy Hamiltonian
  self.turn_nambu() # setup electron-hole if not present
  dd = self.get_multihopping().get_dict() # return the dictionary
  dd = extract_anomalous_dict(dd)
  self.set_multihopping(MultiHopping(dd))
  return self




