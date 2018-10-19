import math, copy

def deg_to_rad ( x ):
    return x * math.pi/180

def rad_to_deg ( x ):
    return x * 180/math.pi

class coordinate( object ):
    def __init__( self, r, theta, phi):
        self.r = r
        self.theta = theta
        self.phi = phi


def spherical_to_cartesian( coord ):
    carte['x'] = coord.r * math.sin(coord.theta) * math.cos(coord.phi)
    carte['y'] = coord.r * math.sin(coord.theta) * math.sin(coord.phi)
    carte['z'] = coord.r * math.cos(coord.theta)
    return carte

def distance( coord1, coord2 ):
    carte1 = spherical_to_cartesian( coord1 )
    carte2 = spherical_to_cartesian( coord2 )
    return math.sqrt( (cart1['x']-cart2['x'])**2 + (cart1['y']-cart2['y'])**2 + (cart1['z']-cart2['z'])**2)




class SatPos( object ):
    _mu = 398601.2
    _earthPeroid = 86164
    _earthRadius = 6378
    _atmosMargin = 150
    
    def __init__( self, coord ):
        self.coord = copy.deepcopy( coord )
        self._initCoord = copy.deepcopy( coord )
    
    def get_altitude( coord ):
        return coord.r - _earthRadius

    def get_latitude( coord ):
        return (math.pi/2 - coord.theta)
    
    def get_longitude( coord ):
        return (math.pi/2 - coord.theta)
    
    def is_visible( coord1, coord2 ):
        dist = distance( coord1, coord2 )
        d = (dist/2)**2
        radius = coord1.r
        grazing_radius = (_earthRadius + _atmosMargin)
        min_radius = math.sqrt(c-d)
        if min_radius >= grazing_radius:
            return True
        return False


class PolarPos( SatPos ):
    def __init__( self, coord, **params ):
        SatPos.__init__( self, coord )

    def update( t ):


    
