from Eccentricity import eccen
import math

class planet:
    def __init__(self, name, ra, rp):
        self.name = name
        self.ra = ra
        self.rp = rp 
        self.a, self.b, self.f = eccen(ra,rp)

    @staticmethod
    def distanceLogConvert(distInAU):
        convertedValue = 8 + math.log(distInAU,2)
        print(convertedValue*26.923)
        return convertedValue*26.923
        
        