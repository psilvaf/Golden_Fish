import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy

def get_ellipse(center: np.ndarray, cova: np.ndarray, nsigma: int = 1, npoints: int = 1000) -> np.ndarray:
    """
    Return the coordinates of a covariance ellipse.

    Args:
        center (np.ndarray): The center of the ellipse.
        cova (np.ndarray): The covariance matrix.
        nsigma (int, optional): The number of standard deviations for the ellipse. Defaults to 1.
        npoints (int, optional): The number of points to generate on the ellipse. Defaults to 1000.

    Returns:
        np.ndarray: The coordinates of the ellipse.
    """
    cholesky_l = np.linalg.cholesky(cova)
    t = np.linspace(0, 2 * np.pi, npoints)
    circle = np.column_stack([np.cos(t), np.sin(t)])
    ellipse = nsigma * circle @ cholesky_l.T + center
    return ellipse.T

def get_params(matrix):
    idx = []
    for m in range(matrix.shape[0]):
        for n in range(m+1,matrix.shape[0]):
            idx.append([m,n])
    idx = np.array(idx)
    mats=[]
    for n in range(idx.shape[0]):
        i,j = idx[n]
        mats.append(np.array([[matrix[i,i],matrix[i,j]],[matrix[j,i],matrix[j,j]]]))
    return mats
    
def plot_ellipse(center,cov_final,par_names,legends):
    fig, ax = plt.subplots()
    ax.set_xlabel(par_names[0])
    ax.set_ylabel(par_names[1])
    colors=['black','salmon','blue'][:len(legends)]
    line_type=['--','-','-'][:len(legends)]
    line_thickness=[1,2,1][:len(legends)]
    for i in range(len(colors)):
        x_sigma, y_sigma = get_ellipse(center, cov_final[i], nsigma=1)
        ax.plot(x_sigma, y_sigma,line_type[i],color=colors[i], label=legends[i],lw=line_thickness[i])
    ax.legend();
    return
