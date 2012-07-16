# vector.py
# Andrew Nguyen Jul 15 2012
# Algorithms for working with vectors

import math

def make_vector(x, y=0, z=0):
    # a, a, a -> vector a
    return [x, y, z]

def lst_to_vector(l):
    # lst a -> vector a
    return l

def get_x(vector):
    # vector a -> a
    return vector[0]

def get_y(vector):
    # vector a -> a
    return vector[1]

def get_z(vector):
    # vector a -> a
    return vector[2]

def vector_len(vector):
    # vector a -> a
    return lst_to_vector(math.sqrt(sum([c**2 for c in vector])))

def normalize(vector):
    # vector a -> vector a
    vlen = vector_len(vector)
    return lst_to_vector([c/vlen for c in vector])

def negate_vector(vector):
    # vector a -> vector a
    return lst_to_vector([-c for c in vector])

def add_vector(vector1, vector2):
    # vector a, vector a -> vector a
    return [a+b for (a,b) in zip(vector1, vector2)]

def sub_vector(vector1, vector2):
    # vector a, vector a -> vector a
    return lst_to_vector(add_vector(vector1, negate_vector(vector2)))

def scale_mul(s, vector):
    # a, vector a -> vector
    return lst_to_vector([s*c for c in vector])

def dot_prod(vector1, vector2):
    return sum([a*b for (a,b) in zip(vector1, vector2)])

def cross_prod(vector1, vector2):
    x = get_y(vector1)*get_z(vector2) - get_y(vector2)*get_z(vector1)
    y = get_z(vector1)*get_x(vector2) - get_z(vector2)*get_x(vector1)
    z = get_x(vector1)*get_y(vector2) - get_x(vector2)*get_y(vector1)
    return lst_to_vector(make_vector(x, y, z))


    




    
