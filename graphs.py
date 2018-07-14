import calcs
import matplotlib.pyplot as plt
import scipy.stats as stats

# pre: series is a Pandas series
def histogram(series):
    plt.hist(series, bins=8)
    plt.title(series.name + " Histogram")
    plt.show()

# pre: series is a Pandas series
def qqplot(series):
    z = calcs.z_scores(series)
    stats.probplot(z, dist="norm", plot=plt)
    plt.title(series.name + " Normal Q-Q plot")
    plt.show()
