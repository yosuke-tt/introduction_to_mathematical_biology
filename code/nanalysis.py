
# coding: utf-8
import numpy as np
import argparse
import matplotlib.pyplot as plt

from time import sleep
import support
from mpl_toolkits.mplot3d import Axes3D
def rungekutta4d( func , argdict = None ,spoint = 0, epoint = 100, initial_value = 1, N = 1000 , numberofvalues = 2 ):
	
      
	h = ( epoint - spoint ) / N
	t = np.arange( spoint, epoint, h )
	
	#１変数の場合
	if numberofvalues == 1:
		
		xpoints = []
		initial_value = np.array( initial_value ).reshape( -1, )
		
		for xx0 in initial_value:
			x = xx0
			xpoint = []
					
			for i, tt in enumerate(t):
				xpoint.append( x )
			
				k1 = h * func( x, t )	
				
				k2 = h * ( func( x + k1 / 2, t + h / 2 ) ) 
				k3 = h * ( func( x + k2 / 2, t + h / 2 ) )
				k4 = h * ( func( x + k3, t + h ) )
				
				x += ( k1 + 2.0 * k2 + 2.0 * k3 + k4 ) / 6
					
				
			xpoints.append( xpoint )
		return t, xpoints
	
	elif numberofvalues == 2:
		
		xpoints = []
		ypoints = []
		
		if isinstance( initial_value, float ) or len( initial_value ) == 0:
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


	elif numberofvalues == 3:
				
		xpoints = []
		ypoints = []
		zpoints = []

		if isinstance( initial_value, float ) or len( initial_value ) == 0  :
			initial_value = [[ 1, 1, 1 ]]
		  
		for iv in initial_value:        
			
			if len(iv) != 3:

				iv = [0.1, 0.1, 0.1] 
			
			xpoint = []
			ypoint = []
			zpoint = []
			

			x = iv[ 0 ]
			y = iv[ 1 ]
			z = iv[ 2 ]
			
			for i, tt in enumerate( t ):
				xpoint.append( x )
				ypoint.append( y ) 
				zpoint.append( z )

				k1 = h * func( x, y, z, tt )[ 0 ]
				l1 = h * func( x, y, z ,tt )[ 1 ]
				m1 = h * func( x, y, z ,tt )[ 2 ]
				
				
				k2 = h * func( x + l1 / 2, y + l1 / 2, z + l1 / 2, tt + h / 2  )[ 0 ] 
				l2 = h * func( x + k1 / 2, y + k1 / 2, z + k1 / 2, tt + h / 2  )[ 1 ] 
				m2 = h * func( x + m1 / 2, y + m1 / 2, z + m1 / 2, tt + h / 2  )[ 2 ] 
				
				k3 = h * func( x + l2 / 2, y + l2 / 2, z + l2 / 2, tt + h / 2  )[ 0 ] 
				l3 = h * func( x + k2 / 2, y + k2 / 2, z + k2 / 2, tt + h / 2  )[ 1 ] 
				m3 = h * func( x + m2 / 2, y + m2 / 2, z + m2 / 2, tt + h / 2  )[ 2 ] 
				
				k4 = h * func( x + l3, y + l3, z + l3, tt + h )[ 0 ] 
				l4 = h * func( x + k3, y + k3, z + k3, tt + h )[ 1 ] 
				m4 = h * func( x + m3, y + m3, z + m3 ,tt + h )[ 2 ] 
				 
				x += ( k1 + 2.0 * k2 + 2.0 * k3 + k4 ) / 6
				y += ( l1 + 2.0 * l2 + 2.0 * l3 + l4 ) / 6
				z += ( m1 + 2.0 * m2 + 2.0 * m3 + m4 ) / 6
				
				

			xpoints.append( xpoint ) 
			ypoints.append( ypoint ) 
			zpoints.append( zpoint )

		return t, xpoints, ypoints, zpoints

def float_to_list( f ):

	if not isinstance( f, list ):
		return [ f ]

	return f

def reshape1n(x):
	return np.array(x).reshape(-1,)


def get_d( points = None ):

	l = np.log10( np.max( points )  ) - 1
	dl = 10 ** int( l )
	dl = round( dl,  int( abs( l ) ) )
	return dl


def graph_plot( t, xpoints, ypoints = None, zpoints = None, chapter = 0, function = None, graph_n = None, hlines = None, vlines = None, linelist = None, savefigOn = True, N = 1000, graph_label = None,  pointplot = None, ntimegraphs = 1, n3dgraphs = 1, additionalplots = None  ):
	
	func_name = function.__class__.__name__

	argdict = { key: val for key, val in function.__dict__.items() if str(key) != "t" and str(key) != "xpoints" and str(key) != "ypoints" and str(key) != "numberofvalues" }        

	print('chapter{}'.format( chapter))			
	print('function             : {}'.format( function.__class__.__name__ ) )
	print('function coefficient : {}'.format( argdict ) )
	

	# 2次元のグラフ作成
	if zpoints == None: 
			
		if ypoints:
			xpoints = float_to_list( xpoints )
			ypoints = float_to_list( ypoints )
			# 時間に対するx, yグラフ
			if ntimegraphs:

				for i, (x, y) in enumerate( zip ( xpoints, ypoints )):
					x = reshape1n( x )
					y = reshape1n( y )
					plt.title( 't-x,y x0 ={}, y0={}, argument : {}'.format( x[ 0 ],y[ 0 ]  , argdict ), fontsize = 7 )
						
					if i > ntimegraphs:
						break
										
					plt.plot( t, x.reshape( -1, ), label = 'x' )
					plt.plot( t, y.reshape( -1, ), label = 'y' )
					plt.title( func_name )
				plt.grid()
				plt.legend()
			   
				
				
			if savefigOn == True:
				plt.savefig('./img/chapter{}/tgraph{}.jpg'.format( chapter, i ) )
				
			plt.show()
			 
		else:
			ypoints = float_to_list( xpoints )
			xpoints = []
			for i in range( len( ypoints ) ):	
				xpoints.append( float_to_list( t ) ) 
				
			
			
		plt.scatter( [], [], label = 'coefficient : {}'.format( argdict ), color = 'k' ) 
		
		for x, y in zip ( xpoints, ypoints ):
					 
			x = reshape1n(x)
			y = reshape1n(y)
			
			plt.plot( x, y, label = 'initial value (x, y) : ({}, {})'.format( x[ 0 ], y[ 0 ] )   )
				
		   

		dx = get_d( xpoints )  
		dy = get_d( ypoints )
			
		y_max, y_min = ( np.max( ypoints )/ 10  - np.max( ypoints )/ 100 ) * 10 + dy , -dy
		x_max, x_min = ( np.max( xpoints )/ 10  - np.max( xpoints )/ 100 ) * 10 + dx , -dx	
		
		plt.xlim( xmin = x_min, xmax = x_max )
		plt.ylim( ymin = y_min, ymax = y_max )

		if not hlines:
			hlines = []
		if not vlines:
			vlines = []
		
			

		plt.title( func_name, loc = 'center')
		
		if len(linelist) > 0:
			p = np.arange( x_min, x_max, 0.01 )
				
			for l in linelist:
				
				if l[ 1 ] == 0:
					vlines.append( l[ 0 ])
				elif l[ 0 ] == 0:
					hlines.append( l[ 1 ] )
				else:
					q = p * l[ 0 ] + l[ 1 ]
					plt.plot( p, q, linestyle = '--')


		if function.numberofvalues == 2 :
			plt.xlabel( "x( t )" )
			plt.ylabel( "y( t )" )
			
		elif function.numberofvalues == 1:
			plt.xlabel( " t " )
			plt.ylabel(" x( t ) ")
			
			
		plt.hlines( y = 0.0, xmin = x_min, xmax = x_max, colors = 'k', linewidths = 2)
		plt.vlines( x = 0.0, ymin = y_min, ymax = y_max, colors = 'k', linewidths = 2)
			
			
		if hlines:
			plt.hlines( y = hlines, xmin = x_min, xmax = x_max,colors = 'lightpink', linewidths = 2, alpha = 0.8, label = 'hlines: {}'.format( hlines ) )
			   
			plt.yticks( list( np.arange( y_min, y_max, dy ) ) + hlines ) 

		if vlines:
			plt.vlines( x = vlines, ymin = y_min, ymax = y_max, colors = 'lightpink', linewidths = 2, alpha = 0.8, label = 'vlines: {}'.format( vlines ) )
			plt.xticks( list(np.arange( x_min, x_max, dx ) ) + vlines, rotation = 45 )

		if pointplot:
			for  p in pointplot:
				plt.scatter( p[0], p[1], s = 20, c = 'r', marker = 'o',label = '{}'.format( p ) )

			
		if additionalplots and  np.array( additionalplots ).shape[0] > 1:
				
			for i, ap in enumerate( additionalplots ) :
					
				if i == 0:
					continue
					
				plt.plot( additionalplots[ 0 ], ap, linestyle = '--' )
		


		plt.grid()
		plt.legend( fontsize = 5, loc = 'upper right', bbox_to_anchor = ( 1, 1 ),  prop = { 'size' : 6 } )



		if savefigOn == True:
			plt.savefig('./img/chapter{}/c{}g{}{}.jpg'.format( chapter,chapter, graph_n, func_name ) )
			
		plt.show()


		for i, ( x, y ) in enumerate( zip( xpoints, ypoints ) ):
					
			if i >= n3dgraphs:
				break
					
			X, Y = np.meshgrid( x, y )
			
			if "get_potential" in dir( function )  and  getattr( function, "get_potential" )( X, Y ).any():
					
				fig = plt.figure( figsize = ( 8, 8 ) )
				ax = fig.add_subplot( 111, projection = "3d" )

				Z = getattr( function, "get_potential" )( X, Y )

				ax.plot_surface( X, Y, Z ) 
					   
				if savefigOn == True:
					plt.savefig('./img/chapter{}/fig3D{}_c{}g{}{}.jpg'.format( chapter, i ,chapter, graph_n, func_name ) )
				plt.show()
			else:
				break
	else:
			
		xpoints = float_to_list( xpoints )
		ypoints = float_to_list( ypoints )
		zpoints = float_to_list( zpoints )

		if ntimegraphs:

			for i, (x, y, z) in enumerate( zip ( xpoints, ypoints, zpoints )):
				x = reshape1n( x )
				y = reshape1n( y )
				z = reshape1n( z )
				plt.title( 't-x,y,z x0 ={}, y0={}, z0={}\n argument : {}'.format( x[ 0 ], y[ 0 ], z[ 0 ]  , argdict ), fontsize = 7 )
					
				if i >= ntimegraphs:
					break

									
				plt.plot( t, x.reshape( -1, ), label = 'x' )
				plt.plot( t, y.reshape( -1, ), label = 'y' )
				plt.plot( t, z.reshape( -1, ), label = 'z' )
				plt.title( func_name )
				plt.grid()
				plt.legend()
			   
				
				
				if savefigOn == True:
					plt.savefig('./img/chapter{}/tgraph{}.jpg'.format( chapter, i ) )
				   
				plt.show()
			
			
		fig = plt.figure( figsize = ( 8, 8 ) )
		ax = fig.add_subplot( 111, projection = "3d" )

		for x, y, z in zip( xpoints, ypoints, zpoints ):
			ax.plot( x, y, z, marker="o",linestyle='None')
			
		ax.set_xlabel("x")
		ax.set_ylabel("y")
		ax.set_zlabel("z")
		ax.plot(x, y, z, marker="o",linestyle='None')
			
		plt.show()

