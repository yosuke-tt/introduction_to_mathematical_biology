import argparse

# def to_num_list( list ):
#     return [ float(f) for f in list]



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

    ps.add_argument('--spoint', '-sp', type = int, default = 0, help = 'start point')
    ps.add_argument('--epoint', '-ep', type = int, default = 1, help = 'end point')
    
    ps.add_argument('--n_epoch', '-n', type = int, help = 'epochs')
    ps.add_argument('--equation_number',  '-e', default = 1, type = int, help = 'equation_number')
    ps.add_argument('--argdict', '-a', nargs = '+', type = float, help = 'equation_number')

    ps.add_argument('--x0','-x0', nargs = '*', type = float, default = 0.01, help = 'x0')
    ps.add_argument('--y0','-y0', nargs = '*', type = float, default = 0.01, help = 'y0')
    ps.add_argument('--savefigoff', '-f', action = 'store_true', default = False , help = 'save figure')
    ps.add_argument('--vline', '-vl', nargs = '+', type = float, help = 'draw vline')
    ps.add_argument('--hline', '-hl', nargs = '+', type = float, help = 'draw hline')
    ps.add_argument('--pointplot', '-pp', nargs = '*', default = None, help = 'draw hline')

    return ps

def seperateby2( pp ):
    if pp and not isinstance(pp[0], list):
        n = ( len( pp ) // 2 ) * 2
        return [ pp[ i: i + 2 ] for i in range( 0, n, 2 ) ]

def offsaving( savefigoff ):
    if savefigoff:
        return False
    else:
        return not savefigoff

