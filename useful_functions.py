import polars as pl
from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.diagnostic import acorr_ljungbox

def check_stationarity(time_series: pl.Series) -> None:
    """Applied the Augmented Dickey Fuller test to check the stationarity of a time series

    Args:
        time_series (pl.Series): polars or pandas series object
    """    
    result = adfuller(time_series)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values: \n', [f"{k} : {float(v)}"  for k,v in result[4].items()])
    if result[1] <= 0.05:
        print("We reject the null hypothesis at 5%.\n",
              "Data most probably has no unit root and is stationary")
    else:
        print("We do not reject the null hypothesis. \n", 
              "Data most probably has a unit root and is non-stationary")
        
        
def perform_lb_test(time_series, lags: int = 30) -> None:
    result = acorr_ljungbox(time_series, lags=[lags], boxpierce=False)
    print('LB Statistic:', float(result['lb_stat'].values[0]))
    print('p-value:', float(result['lb_pvalue'].values[0]))

    # Interpret the results
    p_value = result.iloc[0, 1]
    if p_value < 0.05:
        print("We reject the null hypothesis \n", "There is most probably significant serial correlation in the returns.")
    else:
        print("We do not reject the null hypothesis \n", "There is most probably no significant serial correlation in the returns.")