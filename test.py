import pandas as pd
import os
#테스트용입니다.
df = pd.read_csv('GUI/CSV/test.csv')
df_list = list(df)
df_data = df[df_list[0][0]]
print(df_list)
print(df_data)