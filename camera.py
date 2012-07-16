# camera.py
# Andrew Nguyen Jul 15 2012
# Returns a ray based on geometry

import vector as vr
import ray as ry
import math

def make_view_geometry(eye, up, center):
    # (vector a) ** 3 -> seq (vector a)
    forward = vr.normalize(vr.sub_vector(center, eye))
    side = vr.normalize(vr.cross_prod(forward, up))
    up = vr.normalize(vr.cross_prod(side, forward))
    return [forward, side, up]

def forward(geo):
    return geo[0]

def side(geo):
    return geo[1]

def up(geo):
    return geo[2]

def make_camera(eye, geo, width, height, fovx, fovy):
    def camera(i, j):
        # int, int -> vector a
        alpha = math.tan(fovx/2)*((i - (width/2))/(width/2))
        beta = math.tan(fovy/2)*(((height/2) - j)/(height/2))
        dirn = vr.add_vector(vr.add_vector(vr.scale_mul(alpha, side(geo)),
                                           vr.scale_mul(beta, up(geo))),
                             forward(geo))
        dirn = vr.normalize(dirn)
        return ry.make_ray(eye, dirn)
    return camera

        
    
    
   
    
