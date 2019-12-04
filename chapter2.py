#coding: utf-8
import numpy as np
import nanalysis as na
import support
#import matplotlib
#matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt
from support import Seperateby2



class baseFunction():
    
    def __init__( self ):
        self.xpoints = None
        self.ypoints = None
        self.t = None
        

    def get_values_rungekutta( self, sp = 0, ep = 50, initial_value = [0.1, 0.1] ):

        self.t, self.xpoints, self.ypoints = na.rungekutta4d( self.get_values, spoint = sp, epoint = ep, initial_value = initial_value, var2 = True )
            
        return  self.t, self.xpoints, self.ypoints

 

class lotka_volterra( baseFunction ):
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

        return  [[ -1 / self.a, self.K1 / self.a ], [ -self.b, self.K2 ] ]
    
     

class fujita_model( baseFunction ):
    
    def __init__( self,  r = 0.1, a = 0.3, b = 0.1, c = 0.3 ):
        
        self.r = r
        self.a = a
        self.b = b
        self.c = c

        

    def get_values( self, x, y, t ):

        return self.r * x * ( 1 - self.a * x - self.b * y), -self.c * y + x 

    
    def get_linelist( self ):

        return [ [ - self.a / self.b, 1 / self.b ], [ 1 / self.c, 0 ] ]

    

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
    
    graph = { 1: lotka_volterra , 5 : fujita_model}
    
    if ad:
        function = graph[ graph_n ](**ad)
    else:
        function = graph[ graph_n ]()
    linelist =  function.get_linelist()
    
    if llist:
        linelist.append(llist)
    
    
    t, xpoints, ypoints = function.get_values_rungekutta( sp = sp, ep = ep, initial_value = initial_value )
    
    na.graph_plot( t, xpoints  ,ypoints , chapter = 2, function = function, hlines = hl, vlines = vl, linelist = linelist , savefigOn = saveoff, graph_n = graph_n, N = 10000, pointplot = pp)
