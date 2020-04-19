import pandas as pd
d = {"col1": ["1", "2", "3", "stuff"],
     "col2": ["1", "2", "3", "4"]}
df = pd.DataFrame(d)


def convertToNumeric(column):
    return [float(i) if i.isdigit() else None for i in column]

# pandas method
df.apply(pd.to_numeric, errors="coerce")
