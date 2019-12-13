import argparse
import nanalysis as na
import numpy as np

class BaseFunction(object):
	def __init__( self, numberofvalues = 2 ):
		self.xpoints = None
		self.ypoints = None
		self.zpoints = None
		self.t = None


		self.numberofvalues = numberofvalues 

	def get_values_rungekutta( self, sp = 0, ep = 100, initial_value = [0.1, 0.1], numberofvalues = 2 ):
		if self.numberofvalues == 1:
			self.t, self.xpoints = na.rungekutta4d( self.get_values, spoint = sp, epoint = ep, initial_value = initial_value, numberofvalues = numberofvalues )
	
			return  self.t, self.xpoints, None, None
		
		elif self.numberofvalues == 2:
			self.t, self.xpoints, self.ypoints = na.rungekutta4d( self.get_values, spoint = sp, epoint = ep, initial_value = initial_value, numberofvalues = numberofvalues )
			return  self.t, self.xpoints, self.ypoints, None
		
		elif self.numberofvalues == 3:
			self.t, self.xpoints, self.ypoints, self.zpoints= na.rungekutta4d( self.get_values, spoint = sp, epoint = ep, initial_value = initial_value, numberofvalues = numberofvalues )
			return self.t, self.xpoints, self.ypoints, self.zpoints
	
	def make_adxrange(self):
		additionalplots = []
		xmax = self.xpoints
		xmin = self.xpoints
		while isinstance( xmax, list ):
			xmax = np.amax( self.xpoints )

		while isinstance( xmin, list ):
		   xmin = np.amin( self.xpoints )

		if xmin > 0:
			xmin = 0
		ad_xrange =  np.arange( xmin - 0.1, xmax + 0.1, 0.01 )
		additionalplots.append( ad_xrange )

		return additionalplots
	def get_linelist( self ):
     
		return []


def get_base_args():

    """
    Returns ArgumentParser
    :return: ArgumentParser

    :argument -sp : start_point .
    :argument -ep : end_point .
    :argument -n  : n_epoch .
    :argument -e  : equation_number .
    :argument -a  : function_argument .
    :argument -i  : initial_value .
    :argument -s  : savefig .
    """
    ps = argparse.ArgumentParser( description= 'function argument and value' )

    ps.add_argument('--spoint', '-sp', type = float, default = 0, help = 'start point')
    ps.add_argument('--epoint', '-ep', type = float, default = 10, help = 'end point')
    
    ps.add_argument('--n_epoch', '-n', type = int, help = 'epochs')
    ps.add_argument('--equation_number',  '-e', default = 1, type = int, help = 'equation_number')
    ps.add_argument('--argdict', '-a', type = str, action = Makedict , help = 'function argument dictionary')

    ps.add_argument('--initial_value','-i', nargs = '*', type = float, default = [[ 0.01, 0.01 ]], help = 'x0')
    ps.add_argument('--savefigoff', '-f', action = 'store_true', default = False , help = 'save figure')
    ps.add_argument('--vline', '-vl', nargs = '+', type = float, help = 'draw vline')
    ps.add_argument('--hline', '-hl', nargs = '+', type = float, help = 'draw hline')
    
    ps.add_argument('--pointplot', '-pp', nargs = '*', default = None, help = 'draw hline')
    ps.add_argument('--line', '-l', nargs = '*', default = None ,  help = 'draw line[ a, b ]')
    ps.add_argument( '--n3dgraph', '-n3', type = int, default = 1,help = 'number of showing 3d graph')
    ps.add_argument( '--ntimegraph', '-nt', type = int, default = 1,help = 'number of showing time graph')
   #  ps.add_argument( '--param_graph', '-pg', action - 'store_true', help = 'show param graph') 
    
    return ps


class Makedict( argparse.Action ):
       

    def __call__(self, parser, namespace, values, option_strings=None):
         
        param_dict = getattr(namespace,self.dest,[])

        if param_dict is None:
            param_dict = {}

        k =[ c.strip() for c in values.split( ',' )]
    
        
        param_dict = { kk.split("=")[ 0 ]: float( kk.split("=")[ 1 ]) for kk  in k }
        
        setattr(namespace, self.dest, param_dict)
                                                                                                    
    
def seperatebyN( n = 2, listn = [ 0.1, 0.1, 0.1 ] ):

    nn = ( len( listn ) // n ) * n
    listn = np.array(listn).reshape( -1, )
    listn =  [ listn[ i : i + n ]   for i in range( 0, nn, n ) ]
            
   

    return listn
         
            
             

def offsaving( savefigoff ):
    if savefigoff:
        return False
    else:
        return True
