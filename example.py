
def test_matpyfs(x, y, z):
    xyz = x+y+z
    print 'x = {x}, y = {y}, z={z}, x+y+z={xyz}'.format(**locals())
    return x,y,z,xyz
