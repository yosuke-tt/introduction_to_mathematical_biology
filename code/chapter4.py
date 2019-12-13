import numpy as np
import nanalysis as na
import support
import matplotlib.pyplot as plt
from support import BaseFunction

class Logistic2( BaseFunction ):
	def __init__(self,  r = 2, K = 100 ):
			self.r = r
			self.K = K
			self.numberofvalues = 1

	def get_values( self, x, t ):
		return x + self.r * x * ( 1 - x / self.K )

	def get_linelist( self ):
		return [ [ 0, self.K ] ]


class FujitaAndUtida( BaseFunction ):
	
	def __init__( self, a = 8, b = 2, c = 10 ):

		self.a = a
		self.b = b
		self.c = c

		self.numberofvalues = 1 


	def get_values( self, x, t ):

		return self.a * x / ( 1 + self.b * x ) -  self.c  * x
	
	def get_linelist( self ):
		return [ [ 1 / self.b * ( self.a / self.c - 1 ) , 0 ] ]

class Ricker( BaseFunction ):
	
	def __init__( self, r = 1,  K = 100 ):
        
        
		self.r = r
		self.K = K
		self.numberofvalues = 1 


	def get_values( self, x, t ):

		return x * np.exp( self.r * ( 1 - x / self.K ) ) 



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

	graph = { 1 : Logistic2, 2: FujitaAndUtida, 3: Ricker }

	if ad:
		function = graph[ graph_n ](**ad)
	else:
		function = graph[ graph_n ]()
	linelist =  function.get_linelist()
	
	if llist:
		linelist.append( llist )
	
# t, xpoints, ypoints, zpoints = function.get_values_rungekutta( sp = sp, ep = ep, initial_value = initial_value, numberofvalues = function.numberofvalues )
	t, xpoints = na.numbersequence( function.get_values, epoint = ep, initial_value = initial_value )
	
	adplots = None
	
	if 'get_additionalplots' in dir(function ):
		adplots = function.get_additionalplots()
	
	na.graphplot_NS( t, xpoints = xpoints )
#    na.graph_plot( t, xpoints = xpoints, ypoints = ypoints, zpoints = zpoints, chapter = 4 , function = function, hlines = hl, vlines = vl, linelist = linelist , savefigOn = saveoff, graph_n = graph_n, N = 1000, pointplot = pp, additionalplots = adplots )
