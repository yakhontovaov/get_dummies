import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

print(data)

unique_labels = set(lst)
ohe_dict = {label: (data['whoAmI'] == label).astype(int) for label in unique_labels}
ohe_df = pd.DataFrame(ohe_dict)

data = pd.concat([data, ohe_df], axis=1)

data = data.drop('whoAmI', axis=1)

print(data)
