import pandas as pd

def data_clean():
    data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')

    data = data.set_index('Country code')

    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)

    data_kt = data[data['Series code'] == 'EN.ATM.CO2E.KT']
    data_cd = data[data['Series code'] == 'NY.GDP.MKTP.CD']

    data_kt = data_kt.iloc[:, 5:].replace({'..': pd.np.nan})
    data_cd = data_cd.iloc[:, 5:].replace({'..': pd.np.nan})


    data_kt['CO2-SUM'] = data_kt.sum(axis=1)
    data_cd['GDP-SUM'] = data_cd.sum(axis=1)

    df = pd.concat([data_kt['CO2-SUM'] , data_cd['GDP-SUM']], axis=1)

    df = df.fillna(value = 0)


def co2_gdp_plot():
    
    df_clean = data_clean()
    
    df_max_min = (df_clean - df_clean.min()) / (df_clean.max() - df_clean.min())

    china = []
    for i in df_max_min[df_max_min.index == 'CHN'].values:
        china.extend(np.round(i, 3).tolist())

if __name__ == '__main__':
    data_clean()
