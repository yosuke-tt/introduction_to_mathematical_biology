import numpy as np
import nanalysis as na
import support
import matplotlib
matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt





def lotka_volterra(  x, y, t, r1 = 2, r2 = 1,  K1 = 80, K2 = 70, a = 0.7, b = 1.1 ):
    """
    :param r1, r2 : float : intrinsic rate of natural increase
    :param K1, K2 : float : carrying capacity
    :param a      : float : 
    :param b      : float :
    :return dx/dt, dy/dt : float
    """
    return r1 * x * ( 1 - ( x + a * y ) / K1 ), r2 * y * ( 1 - ( x + a * y ) / K2  )






if __name__ == '__main__':

    graph = { 1: lotka_volterra }

    ps = support.get_base_args()
    args = ps.parse_args()

    graph_n = args.equation_number
    ad = args.argdict

    sp   = args.spoint
    ep   = args.epoint
    x0   = args.x0
    y0   = args.y0
    saveoff = support.offsaving( args.savefigoff )
    hl   = args.hline
    vl   = args.vline
    pp   = support.seperateby2( args.pointplot )


    t, x, y = na.rungekutta4d( graph[ graph_n ], argdict = ad, spoint = sp, epoint = ep, x0 = x0, y0 =  y0, var2 = True)

    function_name = str(graph[ graph_n ].__name__)
    
    print( x[0][:10] )
    print( y[0][:10] ) 




    print( saveoff ) 
    na.graph_plot( t, x, y, chapter = 2, func_name = function_name, hlines = hl, vlines = vl,  argdict = ad,  savefigOn = saveoff, graph_n = graph_n, N = 1000, pointplot = pp)
# X = np.arange( 0, 120, 0.01)
# v = alley( X, 0.03, 100, 20)
# na.graph_plot( v, X, chapter = 1, function_name = 'alley (v-x)', graph_n = 5, func_args = [ 0.03, 100, 20 ],  save_fig = True, pointplot = pp)
