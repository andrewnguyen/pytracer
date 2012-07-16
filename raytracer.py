# raytracer.py
# Andrew Nguyen Jul 15 2012
# Determines if a primitive has been hit

import scene as sc
import ray as ry
import light as lt
import vector as vr

def intersect_lights(scene, lights, pos, normal):
    # scene, light, vector -> float
    color = 1
    for light in lights:
        dirn = vr.normalize(vr.sub_vector(lt.get_pos(light), 
                                                  pos))
        new_ray = ry.make_ray(pos, dirn)
        t, n = intersect_scene(scene, new_ray)
        if not t:
            dot_or_0 = max([vr.dot_prod(dirn, normal), 0])
            incr = dot_or_0*lt.get_brightness(light)
            color += incr
    if color:
        return min([8, color])
    
def intersect_scene(scene, ray):
    # scene, ray -> Maybe (float, vector)
    for prim in scene:
        prim_type = sc.get_type(prim)
        ray = ry.normalize(ray)
        t = sc.intersect(prim_type)(prim, ray)
        if t and t > 0:
            normal =  sc.get_normal(prim_type)(prim, ry.at_t(ray, t) )
            return t, normal
        continue
    return None, None
        
def get_color(scene, lights, ray):
    # scene, lights, ray -> int
    t, normal = intersect_scene(scene, ray)
    ep = 1

    if not t or t <= 0:
        return 0
    if t:
        # calulate new pos...
        new_pos = ry.at_t(ray, t)
        new_pos = vr.add_vector(new_pos, vr.scale_mul(ep, normal))
        return intersect_lights(scene, lights, new_pos, normal)


