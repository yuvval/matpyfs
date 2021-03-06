import argparse
import scipy.io
import importlib
import sys
from numpy import *
import os


def main(args):

    # load the arguments
    inmat = scipy.io.loadmat('{args[infile]}'.format(**locals()))
    if inmat['funcargs'].dtype.names is not None:
        funcargs = {k:inmat['funcargs'][k] for k in inmat['funcargs'].dtype.names}
    else:                    
        funcargs = {}

    # import the module
    module_path = '{args[path]}'.format(**locals())
    sys.path.append(module_path) # Add the module path
    mdl = importlib.import_module('{args[modulename]}'.format(**locals()))
    
    # call the function
    funcargs_str = ', '.join(["%s = funcargs['%s']"%(k,k) for k in funcargs.keys()])
    func_call_cmd = 'mdl.{args[funcname]}({funcargs_str})'.format(**locals())
    res_tuple = eval(func_call_cmd)

    # save the results
    if res_tuple is not None:
        results = {'arg%d'%k:val for k,val in enumerate(res_tuple)}
    else:
        results = {}

    scipy.io.savemat('{args[outfile]}'.format(**locals()), results)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-m','--modulename', help='module name to import', required=True)
    parser.add_argument('-p','--path', help='module path name', required= True)
    parser.add_argument('-f','--funcname', help='function name to call', required=True)
    parser.add_argument('-i','--infile', help='filename holding input arguments', required=True)
    parser.add_argument('-o','--outfile', help='filename holding output arguments', required=True)

    args = vars(parser.parse_args())

    main(args)


