from statsmodels.tsa.stattools import adfuller

def check_stationarity(time_series):
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