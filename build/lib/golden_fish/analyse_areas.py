import numpy as np

def estimate_ellipse_parameters(x_points, y_points):
    
    semi_major_axis = max(x_points) - min(x_points)
    semi_minor_axis = max(y_points) - min(y_points)

    return semi_major_axis, semi_minor_axis

def compute_ellipse_area(semi_major_axis, semi_minor_axis):
    return np.pi * semi_major_axis * semi_minor_axis
    
def area_values(ellip_x,ellip_y):
    '''
    Compute ellipse areas from parameters pairs.
    '''
    semi_major_axis, semi_minor_axis = estimate_ellipse_parameters(ellip_x,ellip_y)
    area = compute_ellipse_area(semi_major_axis, semi_minor_axis)
    return area
