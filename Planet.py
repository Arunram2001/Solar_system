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
        canvasSize = 700
        convertedValue = 8 + math.log(distInAU,2)
        #print(convertedValue*(canvasSize/2)/13)
        return convertedValue*((canvasSize/2)/13)
        
        