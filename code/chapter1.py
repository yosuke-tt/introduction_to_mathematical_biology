import numpy as np
import nanalysis as na
import support
from support import BaseFunction, get_base_args
import matplotlib.pyplot as plt

#m: Malthus 係数
class Exponential( BaseFunction ):
	def __init__( self, m = 3 ):
		self.m = m
		self.numberofvalues = 1
	def get_values( self, x, t ):
		return self.m * x
	
class Logistic( BaseFunction ):
	def __init__(self,  r = 1, K = 100 ):
			self.r = r
			self.K = K
			self.numberofvalues = 1
	def get_values( self, x, t ):
		return self.r * x * ( 1 - x / self.K )

	def get_linelist( self ):
		return [ [ 0, self.K ] ]


class Alley( BaseFunction ):
	def __init__( self, r = 0.03, K = 100, a = 20):
		self.r = r
		self.K = K
		self.a = a
		self.numberofvalues = 1

	def get_values( self, x, t ):
		return self.r * x * ( 1 - x / self.K ) * ( x - self.a )
	
	def get_linelist( self ):
		return [ [ 0, self.K ], [ 0, self.a ] ]

class Yamamura( BaseFunction ):
	
	def	__init__( P = 10 , r = 1.0, K = 100.0 ):
		self.P = P
		self.r = r
		self.K = K
		self.numberofvalues = 1
	def get_values( self, x, t ):
		return self.r * x *( 1 - x /self.K ) - self.P * x**2 / ( 1 + x**2 )




if __name__ == '__main__':

    
	ps = get_base_args()
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

	graph = { 1: Exponential, 2: Logistic, 6: Alley, 4: Yamamura }

	if ad:
		function = graph[ graph_n ](**ad)
	else:
		function = graph[ graph_n ]()
	
	linelist =  function.get_linelist()
	
	if llist:
		linelist.append(llist)
	
	initial_value = np.array( initial_value ).reshape( -1, )

	t,xpoints, ypoints, zpoints = function.get_values_rungekutta( sp = sp, ep = ep, initial_value = initial_value, numberofvalues = function.numberofvalues )
	
	adplots = None 
    
	if 'get_additionalplots' in dir(function ): 
		adplots = function.get_additionalplots()
	
	na.graph_plot( t, xpoints = xpoints, ypoints = ypoints, zpoints = zpoints, chapter = 3 , function = function, hlines = hl, vlines = vl, linelist = linelist , savefigOn = saveoff, graph_n = graph_n, N = 1000, pointplot = pp, ntimegraphs = len( initial_value), additionalplots = adplots )
