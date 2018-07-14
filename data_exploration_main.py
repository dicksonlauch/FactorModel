import util
import graphs

sales_growth_series = util.get_series("SALES_GROWTH")
graphs.histogram(sales_growth_series)
graphs.qqplot(sales_growth_series)