import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

def get_histogram(par,sigma,axes,lt,color): 
    '''par(arr): parameters reference values
    sigma(float): resulting sigma error'''
    x=np.linspace( par-5*sigma,  par+5*sigma, 100000)
    axes.plot(x, stats.norm.pdf(x,par, sigma)/np.max(stats.norm.pdf(x,par, sigma)),color, linestyle=lt)
    return  


