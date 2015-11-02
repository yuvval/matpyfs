function [results] = matpyfs(funcname, funcargs_struct, modulename, modulepath, ...
                             inoutpath, inoutfname_template, pythoncmd)

    if nargin < 5
        inoutpath = '/tmp/';
    end % if nargin < 5

    if nargin < 6
        [~, inoutfname_template] = fileparts(tempname);
    end % if nargin < 5

    if nargin < 7
        pythoncmd = 'python ';
    end % if nargin < 6


    infname = fullfile(inoutpath, [inoutfname_template '_in.mat']);
    outfname = fullfile(inoutpath, [inoutfname_template '_out.mat']);
    
    matpyfs_path = [fileparts(which('matpyfs.m')) '/'];
    funcargs = funcargs_struct;
    save(infname, 'funcargs');

    
    cmd = ([pythoncmd matpyfs_path 'matpyfs.py' ' -f' funcname ' -m ' modulename ' -p' modulepath ...
            ' -i' infname, ' -o' outfname]);
    %    disp(cmd)                           
    system(cmd)
    results = load(outfname);



