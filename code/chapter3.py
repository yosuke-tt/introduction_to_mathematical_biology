import numpy as np
import nanalysis as na
import support
import matplotlib.pyplot as plt
from support import BaseFunction
from support import seperatebyN 
 

class LotkaVolterraModel( BaseFunction ):

   def __init__( self, r =  ,  a = 0.03, b = 0.025, c = 1 ):
        
        
        self.r = r
        self.a = a
        self.b = b
        self.c = c
        self.numberofvalues = 2 

    def get_values( self, x, y, t ):

        return self.r * x - self.a * x * y, self.b * x * y -self.c * y
    
    def get_linelist( self ):

        return [ [ 0, self.r / self.a ], [ self.c / self.b, 0] ]
    
    def get_potential( self, x, y ):
        return -self.c * np.log( x ) + self.b * x - self.r * np.log( y ) + self.a * y 

class LotkaVolterraModel2( BaseFunction ):

    def __init__( self, r = 0.03, K = 100, h = 0.1 ,a = 0.002, b = 0.012, c = 0.1, numberofvalues = 2 ):
        
        self.r = r 
        self.K = K
        self.h = h
        self.a = a
        self.b = b
        self.c = c
        self.numberofvalues = 2  

    def get_values( self, x, y, t ):

        return self.r * x * ( 1 - x /self.K ) - self.a * x * y / ( 1 + self.h * x ), self.b * x * y / ( 1 + self.h * x ) - self.c * y
    
    
    def get_linelist( self ):
             
        return  [ [ self.c / (self.b - self.c * self.h), 0 ] ] 

    
    def get_additionalplots(self):
        adplots = self.make_adxrange()
             
        adplots.append(1 / self.a * ( 1 + self.h * adplots[0] ) * self.r * ( 1 - adplots[0] / self.K ) )
        
        return adplots 

class BasicPandemicModel( BaseFunction ):

    def __init__( self, b = 0.01, c = 1 ):
        """
        b : float : infectious coefficient
        c : float : rate of death or getting better
        """
        self.b = b
        self.c = c
        self.numberofvalues = 2  

    def get_values( self, x, y, t ):

        return -self.b * x * y, self.b * x * y - self.c * y
    
    
    def get_linelist( self ):
             
        return  [ [ self.c / self.b , 0 ] ] 

class AndersonMayModel( BaseFunction ):

    def __init__( self, r = 0.03, b = 0.012, c = 0.1 , e = 0.1 , v = 0.1, numberofvalues = 3 ):
        
        self.r = r
        self.b = b
        self.c = c
        self.e = e
        self.v = v
        self.numberofvalues = 3  
    
    def get_values( self, x, y, z, t ):

        return -self.r *( x + y + z ) - self.b * x * y - self.e * x,\
                self.b*  x * y - ( self.c + self.e + self.v ) * y,\
                self.v * y - self.e * z
    
    


if __name__ == '__main__':

    
    ps = support.get_base_args()
    args = ps.parse_args()

    graph_n = args.equation_number
    ad = args.argdict
    
    sp   = args.spoint
    ep   = args.epoint

    hl   = args.hline
    vl   = args.vline
    llist  =  args.line 
    pp   =  args.pointplot 
    initial_value = args.initial_value
     
    saveoff = support.offsaving( args.savefigoff )
    
    graph = { 1: LotkaVolterraModel , 3 : LotkaVolterraModel2, 4: BasicPandemicModel, 6: AndersonMayModel  }
    
    if ad:
        function = graph[ graph_n ](**ad)
    else:
        function = graph[ graph_n ]()
    
    linelist =  function.get_linelist()
    
    if llist:
        linelist.append(llist)
    
    initial_value = seperatebyN( function.numberofvalues, initial_value )
    
    t,xpoints, ypoints, zpoints = function.get_values_rungekutta( sp = sp, ep = ep, initial_value = initial_value, numberofvalues = function.numberofvalues )
    
    adplots = None
    
    
    if 'get_additionalplots' in dir(function ): 
        
        adplots = function.get_additionalplots()
    
    
    na.graph_plot( t, xpoints = xpoints, ypoints = ypoints, zpoints = zpoints, chapter = 3 , function = function, hlines = hl, vlines = vl, linelist = linelist , savefigOn = saveoff, graph_n = graph_n, N = 1000, pointplot = pp, additionalplots = adplots )
