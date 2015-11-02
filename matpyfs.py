import argparse
import scipy.io
import importlib
from numpy import *


def main(args):

    # load the arguments
    inmat = scipy.io.loadmat('{args[infile]}'.format(**locals()))
    funcargs = {k:inmat['funcargs'][k] for k in inmat['funcargs'].dtype.names}
                            
    # import the module
    mdl = importlib.import_module('{args[modulename]}'.format(**locals()))
    # call the function
    
    res_tuple = eval('mdl.{args[funcname]}(**{funcargs})'.format(**locals()))

    # save the results
    results = {'arg%d'%k:val for k,val in enumerate(res_tuple)}
    scipy.io.savemat('{args[outfile]}'.format(**locals()), results)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-m','--modulename', help='module name to import', required=True)
    parser.add_argument('-f','--funcname', help='function name to call', required=True)
    parser.add_argument('-i','--infile', help='filename holding input arguments', required=True)
    parser.add_argument('-o','--outfile', help='filename holding output arguments', required=True)

    args = vars(parser.parse_args())

    main(args)


