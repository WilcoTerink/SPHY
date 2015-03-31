#-Function to calculate capillary rise
def CapilRise(pcr, etreddry, subfield, subsat, subwater, capmax):
    subrelwat = pcr.max(pcr.min((subwater - subfield) / (subsat - subfield), 1), 0)
    caprise = pcr.min(subwater, capmax * (1 - etreddry) * subrelwat)
    return caprise

#-Function to calculate percolation from subsoil (only if groundwater module is used)
def SubPercolation(pcr, subwater, subfield, subTT, gw, gwsat):
    subperc =  pcr.ifthenelse((gw < gwsat) & ((subwater - subfield) > 0), (subwater - subfield) * (1 - pcr.exp(-1 / subTT)), 0)
    return subperc

#-Function to calculate drainage from subsoil (only if groundwater module is NOT used)
def SubDrainage(pcr, subwater, subfield, subsat, drainvel, subdrainage, subTT):
    subexcess = pcr.max(subwater - subfield, 0)
    subexcessfrac = subexcess / (subsat - subfield)
    sublateral = subexcessfrac * drainvel
    subdrainage = (sublateral + subdrainage) * (1 - pcr.exp(-1 / subTT))
    subdrainage = pcr.max(pcr.min(subdrainage, subwater), 0)
    return subdrainage