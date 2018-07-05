import pandas as pd

def data_clean():
    data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')

    data.set_index('Country code')

    data = data.iloc[:, 5:].replace({'..': pd.np.nan})
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)

    data_kt = data[data['Series code'] == 'EN.ATM.CO2E.KT']
    data_cd = data[data['Series code'] == 'NY.GDP.MKTP.CD']


    data_kt['CO2-SUM'] = data_kt.sum(axis=1)
    data_cd['GDP-SUM'] = data_cd.sum(axis=1)

    df = pd.concat([data_kt['CO2-SUM'] , data_cd]['GDP-SUM'] , axis=1)

    print(df.head())


if __name__ == '__main__':
    data_clean()
