import numpy as np
import nanalysis as na
import support

#m: Malthus 係数
def exponential( x, m  = 3):
    return m * x


def logistic( x, r = 1, K = 100 ):
    """
    :param K (carrying capacity)                    : float.
    :param r (intrinsic rate of natural increase)   : float.
    """
    return r * x * ( 1 - x / K )

def alley( x, r = 0.03, K = 100, a = 20):
    """
    Alle Effect
    :param K (carrying capacity)                    : float.
    :param r (intrinsic rate of natural increase)   : float.
    """
    return r * x * ( 1 - x / K ) * ( x - a )

def yamamura( x, P , r = 1.0, K = 100.0 ):
    return r * x *( 1 - x / K ) - P * x**2 / ( 1 + x**2 )




if __name__ == '__main__':

    graph = { 1: exponential, 2: logistic, 3: alley, 4:yamamura }

    ps = support.get_base_args()
    args = ps.parse_args()

    graph_n = args.equation_number
    fa = args.fucntion_argument
    sp = args.spoint
    ep = args.epoint
    iv = args.initial_value
    save = args.save_fig
    hl = args.hline
    vl = args.vline
    pp = support.seperateby2( args.pointplot )

    iv = np.array(initial_value).reshape(-1)
    t, x = na.runge_kutta_val( graph[ graph_n ], argdict = fa, spoint = sp, epoint = ep, x0 = iv)


    function_name = str(graph[ graph_n ].__name__)

    
    na.graph_plot( t, x, chapter = 1, function_name = function_name, hlines = hl, vlines = vl, argdict = fa, savefigOn = save, graph_n = graph_n, N = 1000, pointplot = pp)


    # X = np.arange( 0, 120, 0.01)
    # v = alley( X, 0.03, 100, 20)
    # na.graph_plot( v, X, chapter = 1, function_name = 'alley (v-x)', graph_n = 5, func_args = [ 0.03, 100, 20 ],  save_fig = True, pointplot = pp)
