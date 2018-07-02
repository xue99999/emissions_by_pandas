import pandas as pd

def data_clean():
    global countries
    data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')
    data = data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    data = data.iloc[:, 5:].replace({'..': pd.np.nan})
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data.dropna(how='all', inplace=True)
    countries = pd.read_excel('ClimateChange.xlsx', sheetname='Country').set_index('Country code')
    return pd.concat([data.sum(axis=1), countries['Income group']], axis=1)

def co2():
    df = data_clean()
    df_sum = df.groupby('Income group').sum()
    df_sum.columns = ['Sum emissions']
    df['haha'] = countries['Country name']
    df_max = df.sort_values(0, ascending=False).groupby('Income group').head(1).set_index('Income group')

    df_max.columns = ['Highest emissions', 'Highest emission country']
    
    df_min = df.sort_values(0).groupby('Income group').head(1).set_index('Income group')
    df_min.columns = ['Lowest emissions', 'Lowest emission country']

    result = pd.concat([df_sum, df_max.sort_index(axis=1), df_min.sort_index(axis=1)], axis=1)
#    return df_max
    return result


if __name__ == '__main__':
    print(co2())
