import numpy as np
import nanalysis as na
import support
import matplotlib.pyplot as plt
from support import BaseFunction


 

class LotkaVolterraModel( BaseFunction ):
    """
    :param r1, r2 : float : intrinsic rate of natural increase
    :param K1, K2 : float : carrying capacity
    :param a      : float : 
    :param b      : float :
    :return dx/dt, dy/dt : float
    """
    def __init__( self, r = 1,  a = 0.03, b = 0.025, c = 1 ):
        
        self.r = r
        self.a = a
        self.b = b
        self.c = c
       

    def get_values( self, x, y, t ):

        return self.r * x - self.a * x * y, self.b * x * y -self.c * y
    
    def get_linelist( self ):

        return [[]]
    
    def get_potential( self, x, y ):
        return None

class LotkaVolterraModel2( BaseFunction ):
    """
    :param r1, r2 : float : intrinsic rate of natural increase
    :param K1, K2 : float : carrying capacity
    :param a      : float : 
    :param b      : float :
    :return dx/dt, dy/dt : float
    """
    def __init__( self, r1 = 1, r2 = 2,  K1 = 80, K2 = 70, a = 0.7, b = 1.1 ):
        
        self.r1 = r1
        self.r2 = r2
        self.K1 = K1
        self.K2 = K2
        self.a = a
        self.b = b

    def get_values( self, x, y, t ):

        return self.r1 * x * ( 1 - ( x + self.a * y ) /self.K1 ), self.r2 * y * ( 1 - (self.b *  x + y ) / self.K2  )
    
    
    def get_linelist( self ):
             
        return  [[],[]]
    
    def get_potential( self, x, y ):
        return None
    

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
    
    graph = { 1: LotkaVolterraModel , 5 : LotkaVolterraModel2 }
    
    if ad:
        function = graph[ graph_n ](**ad)
    else:
        function = graph[ graph_n ]()
    
    linelist =  function.get_linelist()
    
    if llist:
        linelist.append(llist)
    
    
    t, xpoints, ypoints = function.get_values_rungekutta( sp = sp, ep = ep, initial_value = initial_value )
    
    na.graph_plot( t, xpoints  ,ypoints , chapter = 2, function = function, hlines = hl, vlines = vl, linelist = linelist , savefigOn = saveoff, graph_n = graph_n, N = 1000, pointplot = pp)
