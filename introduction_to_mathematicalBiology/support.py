import argparse
import nanalysis as na
# def to_num_list( list ):
#     return [ float(f) for f in list]
class BaseFunction():
    
    def __init__( self ):
        self.xpoints = None
        self.ypoints = None
        self.t = None
        

    def get_values_rungekutta( self, sp = 0, ep = 100, initial_value = [0.1, 0.1] ):

        self.t, self.xpoints, self.ypoints = na.rungekutta4d( self.get_values, spoint = sp, epoint = ep, initial_value = initial_value, var2 = True )
            
        return  self.t, self.xpoints, self.ypoints




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
    ps.add_argument('--epoint', '-ep', type = float, default = 1, help = 'end point')
    
    ps.add_argument('--n_epoch', '-n', type = int, help = 'epochs')
    ps.add_argument('--equation_number',  '-e', default = 1, type = int, help = 'equation_number')
    ps.add_argument('--argdict', '-a', type = str, action = Makedict , help = 'function argument dictionary')

    ps.add_argument('--initial_value','-i', nargs = '*',action = Seperateby2 , type = float, default = [[ 0.01, 0.01 ]], help = 'x0')
    ps.add_argument('--savefigoff', '-f', action = 'store_true', default = False , help = 'save figure')
    ps.add_argument('--vline', '-vl', nargs = '+', type = float, help = 'draw vline')
    ps.add_argument('--hline', '-hl', nargs = '+', type = float, help = 'draw hline')
    
    ps.add_argument('--pointplot', '-pp', nargs = '*', action = Seperateby2, default = None, help = 'draw hline')
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
    
        print(k)
        param_dict = { kk.split("=")[ 0 ]: float( kk.split("=")[ 1 ]) for kk  in k }
        
        setattr(namespace, self.dest, param_dict)
                                                                                                                                
class Seperateby2( argparse.Action ):
    
    def __call__(self, parser, namespace, values, option_strings=None):
        
        pp = getattr(namespace,self.dest,[]) 
        
        if isinstance( values, list ) and not isinstance(values[0], list):
             
            n = ( len( values ) // 2 ) * 2
            pp =  [ [ float( values[ i ] ), float( values[ i + 1 ] ) ]  for i in range( 0, n, 2 ) ]
            
        setattr( namespace, self.dest, pp )     
            
             

def offsaving( savefigoff ):
    if savefigoff:
        return False
    else:
        return not savefigoff


