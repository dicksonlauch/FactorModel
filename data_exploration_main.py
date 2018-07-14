import util
import calcs
import graphs

def normality_tests(series):
    test_statistic , p_value = calcs.shapiro_test(series)
    print(series.name + " Shapiro-Wilk Test statistic value: " + str(test_statistic) + "; P-value: " + str(p_value))
    graphs.histogram(sales_growth_series)
    graphs.qqplot(sales_growth_series)

sales_growth_series = util.get_series("SALES_GROWTH")
normality_tests(sales_growth_series)

