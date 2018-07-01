import pandas as pd

def data_clean():
    data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')

    data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')

    data.drop(labels=['Country code', 'Series name', 'Series code', 'SCALE', 'Decimals'], axis=1, inplace=True)

    data.replace({'..': pd.np.NaN}, inplace=True)

    data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)

    data = data.dropna(how='all', inplace=True)

    data['Sum emissions'] = data.sum(axis=1)

    data = data['Sum emissions']

    countries = pd.read_excel('ClimateChange.xlsx', sheetname='Country')

    countries = countries.set_index('Country code', inplace=True)

    countries.drop(labels=['Capital city', 'Region', 'Lending category'], axis=1, inplace=True)
    
    return pd.concat([data, countries], axis=1)

def co2():
    data = data_clean()

    data = 


