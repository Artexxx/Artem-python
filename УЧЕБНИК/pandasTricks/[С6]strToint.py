import pandas as pd
"""
Надо избавиться от строковых значений в 'SEX'
   Sex  Age --> Age  Sex_female  Sex_male
  male  58      58   0    1
  male  42      42   0    1
female  18      18   1    0
female  24      24   1    0
"""

data = {"Sex": ["male", "male", "female", "female"],
        "Age": [58, 42, 18, 24]}
df = pd.DataFrame(data)


print(pd.get_dummies(df))
