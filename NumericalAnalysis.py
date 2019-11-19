import numpy as np
import argparse
import matplotlib.pyplot as plt 
import pandas as pd


"""
コマンドライン引数の設定
まだない。
これ使うのが好きなのといつか使うだろうからつけとく

"""
def get_base_argument():
    
    ps = argeparse.ArgumentParser()   
    return ps

"""
4次のルンゲクッタ法で1次変数

func1d      : func  : 1変数の1次微分方程式
arg_dict    : dict  : 関数の引数の辞書
spoint      : float : 変数の始点
epoint      : float : 変数の終点
x0          : list  : 境界条件のための始点 
                       f( spoint ) = x0
epochs      : int   : 試行回数
N           : int   : 分割数
"""

def Rungekutta4d_1var( func1d, arg_dict = None, spoint = 0, epoint = 1, x0 = 0, epochs = 100, N = 1000 ):
    
    h = ( ep - sp ) / N
    t = np.arange( sp, ep, h )
    
    xpoints = []

    for xx0 in x0:
        
        x = xx0
        xpoint = []
        
        for i, tt in enumerate( t ):
            xpoint.append( x )
        
            k1 = h * func1d( x, *arg_dict ) 
            k2 = h * ( func1d( x, *arg_dict ) + k1 / 2 ) 
            k3 = h * ( func1d( x, *arg_dict ) + k2 / 2 )  
            k4 = h * ( func1d( x, *arg_dict + k3 ) )
    
            x += ( k1 + 2.0 * k2 + 2.0 * k3 + k4 ) / 6
        
        xpoints.append( xpoint )

    print( 'function name       : %s'%function.__name__ )
    print( 'function argument   : {} '.format( arg_dict ) )
    print( 'initial value       : {} '.format( x0 ) )

    return t, xpoints

def Rungekutta4d_2var( function, function_argument, start_point, end_point, initial_value, epochs = 1000 ):


