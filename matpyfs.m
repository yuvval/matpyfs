function [results] = matpyfs(funcname, funcargs_struct, modulename, modulepath, ...
                             pythoncmd, inoutpath, inoutfname_template)

    if nargin < 5
        pythoncmd = 'python';
    end % if nargin 

    if nargin < 6
        inoutpath = '/tmp/';
    end % if nargin 

    if nargin < 7
        [~, inoutfname_template] = fileparts(tempname);
    end % if nargin 



    infname = fullfile(inoutpath, [inoutfname_template '_in.mat']);
    outfname = fullfile(inoutpath, [inoutfname_template '_out.mat']);
    
    matpyfs_path = [fileparts(which('matpyfs.m')) '/'];
    funcargs = funcargs_struct;
    save(infname, 'funcargs');

    
    cmd = ([pythoncmd ' ' matpyfs_path 'matpyfs.py' ' -f' funcname ' -m ' modulename ' -p' modulepath ...
            ' -i' infname, ' -o' outfname]);
    %    disp(cmd)                           
    system(cmd)
    results = load(outfname);



