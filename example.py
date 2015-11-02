
def test_matpyfs(x, y, z):
    xyz = x+y+z
    print 'x = {x}, y = {y},={xyz}'.format(**locals())
    return x,y,z,xyz
