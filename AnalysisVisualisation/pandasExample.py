import pandas as pd

decay_df = pd.read_csv("many_decays.csv")

print(decay_df.count())
print(decay_df.dropna())
