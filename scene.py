# scene.py
# Andrew Nguyen Jul 15 2012
# Holds information about the scene and primitives

import ray as ry
import vector as vr
import math

def make_sphere(center, radius):
    # vector a, a -> sphere a
    return ([center, radius], "sphere")

def get_center(sphere):
    return sphere[0][0]

def get_radius(sphere):
    return sphere[0][1]

def get_type(prim):
    return prim[1]

def intersect_sphere(sphere, ray):
    # sphere a, ray a -> Maybe int
    dirn = ry.get_dirn(ray)
    pos = ry.get_pos(ray)
    center = get_center(sphere)
    to_center = vr.sub_vector(pos, center)
    a = vr.dot_prod(dirn, dirn)
    b = 2*vr.dot_prod(dirn, to_center)
    c = vr.dot_prod(to_center, to_center) - get_radius(sphere) ** 2
    det = b ** 2 - 4 * a * c
    if det < 0:
        return None
    else:
        print ("ABC: ", a, b, c)
        t1 = (-b + math.sqrt(det)) / (2*a)
        t2 = (-b - math.sqrt(det)) / (2*a)
        return min([t1, t2])

def sphere_normal(sphere, pt):
    print("PT: ", pt)
    return vr.normalize(vr.sub_vector(pt, get_center(sphere)))

intersectors = {"sphere": intersect_sphere}
def intersect(prim_type):
    # type -> fn
    return intersectors[prim_type]

normals = {"sphere": sphere_normal}
def get_normal(prim_type):
    # type -> fn
    return normals[prim_type]
    
    
