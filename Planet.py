from Eccentricity import eccen

class planet:
    def __init__(self, name, ra, rp):
        self.name = name
        self.ra = ra
        self.rp = rp 
        self.a, self.b, self.f = eccen(ra,rp)
        