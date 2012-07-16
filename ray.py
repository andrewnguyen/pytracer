# ray.py
# Andrew Nguyen Jul 15 2012
# Constructs a ray

import vector as vr

def make_ray(pos, dirn):
    # vector a, vector b -> ray a
    return [pos, dirn]

def get_pos(ray):
    return ray[0]

def get_dirn(ray):
    return ray[1]

def normalize(ray):
    # ray -> ray
    dirn = vr.normalize(get_dirn(ray))
    return make_ray(get_pos(ray), dirn)

def ray_len(ray):
    return vr.vector_len(get_dirn(ray))

def at_t(ray, t):
    # ray, float -> vector
    pos = get_pos(ray)
    dirn = get_dirn(ray)
    new_pos = vr.add_vector(pos, vr.scale_mul(t, dirn))
    return new_pos
    
