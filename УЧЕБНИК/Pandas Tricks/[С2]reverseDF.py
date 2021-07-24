"""
A B C -> C B A
1 2 3    3 2 1
"""
import pandas as pd
df = pd.read_csv('data/intSimple.csv')

# Reverse column order
df.loc[:, ::-1]
# Reverse row order
df.loc[::-1]
# Reverse row order and reset index
df.loc[::-1].reset_index(drop=True)