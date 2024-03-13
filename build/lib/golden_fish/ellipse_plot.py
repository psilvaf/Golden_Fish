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
    
def plot_ellipse(center,cov_final,par_names,legends):
    fig, ax = plt.subplots()
    ax.set_xlabel(par_names[0])
    ax.set_ylabel(par_names[1])
    colors=['blue','salmon','black']
    line_type=['-','-','--']
    line_thickness=[1,4,1]
    for i in range(len(colors)):
        x_sigma, y_sigma = get_ellipse(center, cov_final[i], nsigma=1)
        ax.plot(x_1sigma, y_1sigma,color=colors[i], label=legends[i],lw=line_thickness[i])
    ax.legend();
    return
