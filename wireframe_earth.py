'''
Wireframe Earth is the first Rocket Appliance. It is a graticule of coordinates
that approximates the Earth's surface.
Broadly speaking, the Wireframe Earth has two properties: the ellipsoid and
the graticule.

The ellipsoid is a solid geometric construct. In complexity and geodesic fidelity,
it can range from a sphere to a geoid. It has the following basic properties:

 - center: the geometric point corresponding to the center of mass
 - axis of rotation: a line passing through the center and both poles
 - vector of rotation: parallel to axis of rotation, by convention pointing north; 
    magnitude is, per [Wikipedia](), "angular speed of Earth's rotation in inertial 
    space is (7.2921150 ± 0.0000001) ×10−5 radians per SI second (mean solar second).
    Multiplying by (180°/π radians)×(86,400 seconds/mean solar day) yields 360.9856°/mean solar day"
  - mean radius: 6371.0 km
  - equatorial radius: 6378.1 km
  - polar radius: 6356.8 km
  - flattening: 0.0033528 or 1/298.257222101
  
The graticule is composed of two angles, longitude and latitude. These angles can be expressed as:
 - degrees min sec ( a tuple of  sense, integer zero to max, integer zero to 59, float 0.00 less thnn 60 )
 - fractional degrees ( a tuple of sense, integer zero to max, float  )
 - radians
'''
