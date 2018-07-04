import pandas as pd

def co2_gdp_plot():
    data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')
    data = data.set_index('Country code')
    data = data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    data = data[data['Series code'] == 'NY.GDP.MKTP.CD'].set_index('Country code')
    data = data.iloc[:, 5:].replace({'..': pd.np.nan})
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)

    print(data.head())


if __name__ == '__main__':
    co2_gdp_plot()
