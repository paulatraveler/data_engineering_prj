import pandas as pd

#df=pd.read_csv('data.csv',header=None, names=["bone", "muscle","number"])


def calculate(df: pd.DataFrame)->list:
    means = df.groupby(['bone']).mean()
    stdevs = df.groupby(['muscle']).std()

    result = []

    for index, row in df.iterrows():
        if (index+1) % 2 == 1:
            elem = means.loc[row.bone][0]
        else:
            elem = stdevs.loc[row.muscle][0]
        result.append(elem)

    return result


