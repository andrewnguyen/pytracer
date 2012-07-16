# light.py
# Andrew Nguyen Jul 15 2012
# Algorithms for working with lights

import vector as vr

def make_light(x, y, z, b):
    # a, a, a, a-> light
    return (vr.make_vector(x, y, z), b)

def get_pos(light):
    # light -> vector a
    return light[0]

def get_x(light):
    # light a -> a
    return vr.get_x(get_pos(light))

def get_y(light):
    # light a -> a
    return vr.get_y(get_pos(light))

def get_z(light):
    # light a -> a
    return vr.get_z(get_pos(light))

def get_brightness(light):
    # light a -> a
    return light[1]
