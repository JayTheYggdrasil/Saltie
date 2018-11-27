import numpy as np
from RLUtilities.LinearAlgebra import vec3

def magnitude(vec: vec3):
    return (vec[0]**2 + vec[1]**2 + vec[2]**2)**0.5

def direction(vec: vec3):
    return vec/magnitude(vec)

def parse_vec(vec: vec3):
    return np.array( [vec[0], vec[1], vec[2]] )

def to_vec( numpyarr ):
    return vec3( numpyarr[0], numpyarr[1], numpyarr[2] )
