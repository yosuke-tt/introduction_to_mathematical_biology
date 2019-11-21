import matplotlib
matplotlib.use('Agg')
import numpy as np
import argparse
import matplotlib.pyplot as plt
from time import sleep



def rungekutta4d( func , argdict  = None, spoint = 0, epoint = 1, x0 = 0, y0 = 0, N = 1000 , var2 = False):
    """
    Returns t xpoints
    :param func         : func   : 微分方程式.
    :param func2        : func.  : 2個目の微分方程式
    :param argdict      : dict       : 引数のdict 
    :param argdict2     : dict       : 二つ目の関数の引数のdict 
    :param spoint       : float      : 時間tの始点
    :param end_point    : float　　　: 時間tの終点
    :pram N             : int        : 分割数
    :pram x0            : float　　　: 関数1の始点 func( spoint )  = x0
    :pram y0            : float　　　: 関数2の始点 func2( spoint ) = y0
    :return float list of xpoints, float list of t
    """

    if str( type( x0 ) )  == "<class 'float'>":
        x0 = [ x0 ]
    
    if str( type( y0 ) )  == "<class 'float'>":
        y0 = [ y0 ]

    
    h = ( epoint - spoint ) / N

    t = np.arange( spoint, epoint, h )

    if var2 == False :

        xpoints = []
        for xx0 in x0:

            x = xx0
            xpoint = []

            for i, tt in enumerate(t):
                xpoint.append( x )
                if argdict:
                    k1 = h * func( x, **argdict)
                    k2 = h * ( func( x, **argdict  ) + k1 / 2)
                    k3 = h * ( func( x, **argdict  ) + k2 / 2)
                    k4 = h * ( func( x, **argdict ) + k3 )
                    x += ( k1 + 2.0 * k2 + 2.0 * k3 + k4 ) / 6

                else:
                    k1 = h * func( x )
                    k2 = h * ( func( x ) + k1 / 2)
                    k3 = h * ( func( x  ) + k2 / 2)
                    k4 = h * ( func( x ) + k3 )
                    x += ( k1 + 2.0 * k2 + 2.0 * k3 + k4 ) / 6

            xpoints.append( xpoint )

        print('func : {}'.format( func.__name__ ) )
        print('func arguments : {}'.format( argdict ) )
        print('initial value : {}'.format( x0 ) )

        return t, xpoints

    else:

        xpoints = []
        ypoints = []

        for xx0, yy0 in zip( x0 , y0 ):

            xpoint = []
            ypoint = []
            
            x = xx0
            y = yy0

            for i, tt in enumerate( t ):
                xpoint.append( x )
                ypoint.append( y ) 

 
                if argdict:
                    k1, _ = h * func( x, y, t, **argdict )
                    _, l1 = h * func( x, y, t, **argdict )
                    
                    k2, _ = h *  func( x + l1 / 2, y + l1 / 2, t + h / 2, **argdict  ) 
                    _, l2 = h *  func( x + k1 / 2, y + k1 / 2, t + h / 2, **argdict  ) 
                
                    k3, _ = h *  func( x + l2 / 2, y + l2 / 2, t + h / 2, **argdict  ) 
                    _, l3 = h *  func( x + k2 / 2, y + k2 / 2, t + h / 2, **argdict  ) 
                
                
                    k4, _ = h * func( x + l3, y + l3, t + h, **argdict ) 
                    _,l4 = h * func( x + k3, y + k3, t + h, **argdict ) 
                
                    x += ( k1 + 2.0 * k2 + 2.0 * k3 + k4 ) / 6
                    y += ( l1 + 2.0 * l2 + 2.0 * l3 + l4 ) / 6
           
                else:

                    
                    k1 = h * func( x, y, t )[ 0 ]
                    l1 = h * func( x, y, t )[ 1 ]
                    
                    k2 = h *  func( x + l1 / 2, y + l1 / 2, t + h / 2  )[ 0 ] 
                    l2 = h *  func( x + k1 / 2, y + k1 / 2, t + h / 2  )[ 1 ]
                
                    k3 = h *  func( x + l2 / 2, y + l2 / 2, t + h / 2  )[ 0 ] 
                    l3 = h *  func( x + k2 / 2, y + k2 / 2, t + h / 2  )[ 1 ]
                
                
                    k4 = h * func( x + l3, y + l3, t + h )[ 0 ] 
                    l4 = h * func( x + k3, y + k3, t + h )[ 1 ] 
                
                    x += ( k1 + 2.0 * k2 + 2.0 * k3 + k4 ) / 6
                    y += ( l1 + 2.0 * l2 + 2.0 * l3 + l4 ) / 6
           


            xpoints.append( xpoint ) 
            ypoints.append( ypoint ) 

        return t,xpoints, ypoints

def float_to_list( f ):

    if not isinstance( f, list ):
        return [ f ]
    
    return f


def graph_plot( t, xpoints, ypoints = None, chapter = 0, func_name = None, graph_n = None, hlines = None, vlines = None, argdict = None, savefigOn = True, N = 1000, graph_label = None,  pointplot = None, Ntimegraphs = [1] ):

        """
        Returns t xpoints
        :pram xpoints       : float list.
        :param t            : float list.
        :param func     : str
        :param graph_n      : int
        :param argdict: float list.
        :param save_fig     : boolen
        :pram N             : int
        """
        
        if ypoints:
            xpoints = float_to_list( xpoints )
            ypoints = float_to_list( ypoints )

            for i in range( *Ntimegraphs ):

                plt.title( 't-x,y x0 ={}, y0={}, argument : {}'.format( xpoints[i][0], ypoints[i][0], argdict ) )
                plt.plot( t, xpoints[i], label = 'x' )
                plt.plot( t, ypoints[i], label = 'y' )
                plt.grid()
                plt.legend()
                
                if savefigOn:
                    plt.savefig( './img/chapter{}/tgraph{}.jpg'.format( chapter, i ) )

                plt.close()   
                

        else:
            xpoints = float_to_list( t )
            ypoints = float_to_list( xpoints )

        

        
        for x in xpoints:
            for y in ypoints:

                plt.plot ( x, y, label = 'initial value (x, y) : {:>5}{:>5}, func argument :{}'.format( x[ 0 ], y[ 0 ], argdict) )


        plt.grid()

        dy = ( np.max( ypoints ) - np.min( ypoints ) ) / 30
        dx = ( np.max( xpoints ) - np.min( xpoints ) ) / 30
        ddy = ( np.max( ypoints ) - np.min( ypoints ) ) / 10
        ddx = ( np.max( xpoints ) - np.min( xpoints ) ) / 10
        y_max, y_min = np.max( ypoints ) + dy, np.min( ypoints ) - dy
        x_max, x_min = np.max( xpoints ) + dx, np.min( xpoints ) - dx

        plt.xlim( xmin = x_min, xmax = x_max )
        plt.ylim( ymin = y_min, ymax = y_max )

        plt.hlines( y = 0.0, xmin = x_min, xmax = x_max, colors = 'k', linewidths = 2)
        plt.vlines( x = 0.0, ymin = y_min, ymax = y_max, colors = 'k', linewidths = 2)

        if hlines:
            plt.hlines( y = hlines, xmin = x_min, xmax = x_max,colors = 'k', linewidths = 2, alpha = 0.8, label = 'hlines: {}'.format( hlines ) )
            plt.yticks( list( np.arange( y_min, y_max, ddy ) ) + hlines)

        if vlines:
            plt.vlines( x = vlines, ymin = y_min, ymax = y_max, colors = 'k', linewidths = 2, alpha = 0.8, label = 'vlines: {}'.format( vlines ) )
            plt.xticks( list(np.arange( x_min, x_max, ddx )) + vlines)

        if pointplot:
            for  p in pointplot:
                plt.scatter( p[0], p[1], s = 20, c = 'r', marker = 'o',label = '{}'.format( p ) )



        plt.title( func_name , loc = 'left')

        if ypoints:
            plt.xlabel( "x( t )" )
            plt.ylabel( "y( t )" )
        else:
            plt.xlabel( " t " )
            plt.ylabel(" y( t ) ")

        plt.legend( fontsize = 10, loc = 'lower right', bbox_to_anchor = ( 1, 1 ),  prop = { 'size' : 6 } )

        if savefigOn == True:
            plt.savefig('./img/chapter{}/c{}g{}{}.jpg'.format( chapter,chapter, graph_n, func_name ) )

        plt.show()
