import pandas as pd

df = pd.read_csv('file2.csv')

data_types = df.dtypes

for column in data_types.index:
    if data_types[column] == 'datetime64[ns]':
        print(column + ': date')
    elif data_types[column] == 'int64':
        print(column + ' : int')
    elif data_types[column] == 'float64':
        print(column + ': float')
    elif data_types[column] == 'object':
        if len(df[column].unique()) == 1:
            print(column + ': char')
        elif df[column].str.isnumeric().all():
            print(column + ': int')
        elif df[column].str.isdecimal().all():
            print(column + ': float')
        elif len(df[column].unique()) < len(df[column]):
            print(column + ': enum')
        else:
            print(column + ': string')
