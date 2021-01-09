import pandas as pd

df = pd.read_csv("test_data.csv")

k = df.loc[df.source_id == 39].reset_index().at[0, 'id']


