import numpy as np
import scipy.stats as stats

def z_scores(series):
    return (series - np.mean(series)) / np.std(series)

def shapiro_test(series):
    return stats.shapiro(series)