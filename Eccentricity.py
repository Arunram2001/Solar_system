from math import sqrt

def eccen(ra,rp):
    rsum = ra+rp
    rdiff = ra-rp
    eccentricity = rdiff/rsum
    a = rsum/2
    b = a*sqrt(1-(eccentricity**2))
    f = eccentricity*a
    return a, b, f