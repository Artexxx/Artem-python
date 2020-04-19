import pandas as pd
df = pd.read_csv('data/intSimple.csv')


def addPrefix(df, prefix):
    df.columns = [prefix + i for i in df.columns]

# pandas methods
df.add_prefix("A_")
df.add_suffix("_Z")
