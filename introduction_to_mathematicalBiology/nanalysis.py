
# coding: utf-8
import numpy as np
import argparse
import matplotlib.pyplot as plt

from time import sleep
import support
from mpl_toolkits.mplot3d import Axes3D


def rungekutta4d( func , argdict = None ,spoint = 0, epoint = 1, initial_value = 1, N = 1000 , var2 = False):
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

    if str( type( initial_value ) )  == "<class 'float'>":
        x0 = [ x0 ]
    

    
    h = ( epoint - spoint ) / N

    t = np.arange( spoint, epoint, h )

    if var2 == False :

        xpoints = []
        
        for xx0 in initial_value:

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

        if isinstance( initial_value, float ):
            initial_value = [[ 1, 1 ]]
         
        for iv in initial_value:        
            xpoint = []
            ypoint = []
            

            x = iv[ 0 ]
            y = iv[ 1 ]
            for i, tt in enumerate( t ):
                xpoint.append( x )
                ypoint.append( y ) 
                                   
                k1 = h * func( x, y, tt )[ 0 ]
                l1 = h * func( x, y, tt )[ 1 ]
                    
                k2 = h *  func( x + l1 / 2, y + l1 / 2, tt + h / 2  )[ 0 ] 
                l2 = h *  func( x + k1 / 2, y + k1 / 2, tt + h / 2  )[ 1 ]
                
                k3 = h *  func( x + l2 / 2, y + l2 / 2, tt + h / 2  )[ 0 ] 
                l3 = h *  func( x + k2 / 2, y + k2 / 2, tt + h / 2  )[ 1 ]
                
                
                k4 = h * func( x + l3, y + l3, tt + h )[ 0 ] 
                l4 = h * func( x + k3, y + k3, tt + h )[ 1 ] 
                 
                x += ( k1 + 2.0 * k2 + 2.0 * k3 + k4 ) / 6
                y += ( l1 + 2.0 * l2 + 2.0 * l3 + l4 ) / 6
                
            
        
            xpoints.append( xpoint ) 
            ypoints.append( ypoint ) 
           
        return t,xpoints, ypoints

def float_to_list( f ):

    if not isinstance( f, list ):
        return [ f ]
    
    return f

def reshape1n(x):
    return np.array(x).reshape(-1,)

def graph_plot( t, xpoints, ypoints = None, chapter = 0, function = None, graph_n = None, hlines = None, vlines = None, linelist = None, savefigOn = True, N = 1000, graph_label = None,  pointplot = None, ntimegraphs = 1, n3dgraphs = 1  ):

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
        
        func_name = function.__class__.__name__ 
        argdict = { key: val for key, val in function.__dict__.items() if str(key) != "t" and str(key) != "xpoints" and str(key) != "ypoints" }        
        
        if ypoints:
            xpoints = float_to_list( xpoints )
            ypoints = float_to_list( ypoints )

            if ntimegraphs:

                for i, (x, y) in enumerate( zip ( xpoints, ypoints )):
                    x = reshape1n( x )
                    y = reshape1n( y )
                    plt.title( 't-x,y x0 ={}, y0={}, argument : {}'.format( x[ 0 ],y[ 0 ]  , argdict ) )
                    if i >= ntimegraphs:
                        break
                    
                    plt.plot( t, x.reshape(-1,), label = 'x' )
                    plt.plot( t, y.reshape(-1,), label = 'y' )
                plt.grid()
                plt.legend()
               
                
                
                if savefigOn == True:
                    plt.savefig('./img/chapter{}/tgraph{}.jpg'.format( chapter, i ) )
                
                plt.show()
                
                                
                

        else:
            xpoints = float_to_list( t )
            ypoints = float_to_list( xpoints )

           
        
        for x, y in zip(xpoints, ypoints):
            x = reshape1n(x)
            y = reshape1n(y)
                
            plt.plot( x, y, label = 'initial value (x, y) : ({}, {}), func argument :{}'.format( x[ 0 ], y[ 0 ], argdict )   )
        
        
        
        

        dy = ( np.max( ypoints ) - np.min( ypoints ) ) / 30
        dx = ( np.max( xpoints ) - np.min( xpoints ) ) / 30
        ddy = ( np.max( ypoints ) - np.min( ypoints ) ) / 10
        ddx = ( np.max( xpoints ) - np.min( xpoints ) ) / 10
        y_max, y_min = np.max( ypoints ) + dy, np.min( ypoints ) - dy
        x_max, x_min = np.max( xpoints ) + dx, np.min( xpoints ) - dx
        
   
        plt.xlim( xmin = x_min, xmax = x_max )
        plt.ylim( ymin = y_min, ymax = y_max )

        if not hlines:
            hlines = []
        if not vlines:
            vlines = []


        plt.title( function.__class__.__name__, loc = 'left')

        if ypoints and linelist[0]:
            plt.xlabel( "x( t )" )
            plt.ylabel( "y( t )" )
            
            p = np.arange( x_min, x_max, 0.01 )
            
            for l in linelist:
                plt.plot()

        elif ypoints:
            plt.xlabel( "x( t )" )
            plt.ylabel( "y( t )" )
            
        else:
            plt.xlabel( " t " )
            plt.ylabel(" y( t ) ")
        
        
        plt.hlines( y = 0.0, xmin = x_min, xmax = x_max, colors = 'k', linewidths = 2)
        plt.vlines( x = 0.0, ymin = y_min, ymax = y_max, colors = 'k', linewidths = 2)

        if hlines:
            plt.hlines( y = hlines, xmin = x_min, xmax = x_max,colors = 'lightpink', linewidths = 2, alpha = 0.8, label = 'hlines: {}'.format( hlines ) )
            plt.yticks( list( np.arange( y_min, y_max, ddy ) ) + hlines)

        if vlines:
            plt.vlines( x = vlines, ymin = y_min, ymax = y_max, colors = 'lightpink', linewidths = 2, alpha = 0.8, label = 'vlines: {}'.format( vlines ) )
            plt.xticks( list(np.arange( x_min, x_max, ddx )) + vlines)

        if pointplot:
            for  p in pointplot:
                plt.scatter( p[0], p[1], s = 20, c = 'r', marker = 'o',label = '{}'.format( p ) )


        plt.grid()
        plt.legend( fontsize = 5, loc = 'lower right', bbox_to_anchor = ( 1, 1 ),  prop = { 'size' : 6 } )

        if savefigOn == True:
            plt.savefig('./img/chapter{}/c{}g{}{}.jpg'.format( chapter,chapter, graph_n, func_name ) )
        
        plt.show()


        for i, ( x, y ) in enumerate( zip( xpoints, ypoints ) ):
                
            if i >= n3dgraphs:
                break
                
            X, Y = np.meshgrid( x, y )
            
            if getattr( function, "get_potential" )( X, Y ):
                
                fig = plt.figure( figsize = ( 8, 8 ) )
                ax = fig.add_subplot( 111, projection = "3d" )

                Z = getattr( function, "get_potential" )( X, Y )

                ax.plot_surface( X, Y, Z ) 
                   
                if savefigOn == True:
                    plt.savefig('./img/chapter{}/fig3D{}_c{}g{}{}.jpg'.format( chapter, i ,chapter, graph_n, func_name ) )
                plt.show()
            else :
                break
