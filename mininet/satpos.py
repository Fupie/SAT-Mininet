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
    carte = {}
    carte['x'] = coord.r * math.sin(coord.theta) * math.cos(coord.phi)
    carte['y'] = coord.r * math.sin(coord.theta) * math.sin(coord.phi)
    carte['z'] = coord.r * math.cos(coord.theta)
    return carte

def distance( coord1, coord2 ):
    carte1 = spherical_to_cartesian( coord1 )
    carte2 = spherical_to_cartesian( coord2 )
    return math.sqrt( (cart1['x']-cart2['x'])**2 + (cart1['y']-cart2['y'])**2 + (cart1['z']-cart2['z'])**2)


class Pos( object ):
    _mu = 398601.2
    _earthPeroid = 86164
    _earthRadius = 6378
    _atmosMargin = 150

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

class TPos( Pos ):
    def __init__(self, lat, lon):
        r = Pos._earthRadius
        assert lat >=-90 and lat <= 90
        theta = deg_to_rad(90 - lat)

        assert lon >=-180 and lon <= 180
        if lon < 0:
            phi = deg_to_rad( 360 + lon )
        else:
            phi = deg_to_rad(lon)
        self._coord = coordinate(r, theta, phi)
        

class PolarPos( Pos ):
    _time_advance = 0
    def __init__( self, alt, lon, alpha, incl):
        assert alt > 0
        r = alt + Pos._earthRadius
        
        assert alpha >=0 and alpha <= 360
        theta = deg_to_rad(alpha)

        assert lon >=-180 and lon <= 180
        if lon < 0:
            phi = deg_to_rad( 360 + lon )
        else:
            phi = deg_to_rad(lon)

        assert incl >= 0 and incl <= 180
        self._inclination = deg_to_rad(incl)
        self._period = 2 * math.pi * math.sqrt(r**3/Pos._mu)
        self._initial = coordinate(r,theta,phi)
        self._coord = copy.deepcopy(self._initial)

    def update( self, t ):
        partial = (math.fmod( t + self._time_advance, self._period )/self._period)*2*math.pi
        theta_cur = math.fmod( self._initial.theta + partial, 2*math.pi)
        phi_cur = self._initial.phi
        assert self._inclination<math.pi
        theta_new = math.pi/2 - math.asin( math.sin(self._inclination) * math.sin(theta_cur))
        if theta_cur > math.pi/2 and theta_cur < 3*math.pi/2:
            phi_new = math.atan( math.cos(self._inclination) * math.tan(theta_cur)) + phi_cur + math.pi
        else:
            phi_new = math.atan( math.cos(self._inclination) * math.tan(theta_cur)) + phi_cur

        phi_new = math.fmod(phi_new + 2*math.pi, 2*math.pi)
        self._coord.theta = theta_new
        self._coord.phi = phi_new
        '''print self._coord.r, self._coord.theta, self._coord.phi'''
