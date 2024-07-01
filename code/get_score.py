from getpublicvsprivatespent import get_public_vs_private
import pandas as pd
import numpy as np

data = pd.read_csv('data\Visa Climate Tech Data.xlsx - 2_Card data.csv')

data = data['cluster_name_adjusted'].unique()
public_vs_private_spent = {}

for cluster_name_adjusted in data:
    public_vs_private_spent[cluster_name_adjusted] = get_public_vs_private(cluster_name_adjusted)


def get_ratio(public_vs_private_spent):
    ratio = {}
    for cluster_name_adjusted, (public, private) in public_vs_private_spent.items():
        ratio[cluster_name_adjusted] = public / private
    return ratio

ratio = get_ratio(public_vs_private_spent)


#get mean and standard deviation of the ratios
mean = np.mean(list(ratio.values()))
std = np.std(list(ratio.values()))

#above 80 percentile is A+ , 60-80 is A, 40-60 is B, 20-40 is C, 0-20 is D
def get_overall_score(cluster_name_adjusted):
    public ,private = get_public_vs_private(cluster_name_adjusted)
    ratio = public / private
    score = (ratio - mean) / std
    if score > 1.28:
        return 'A+'
    elif score > 0.84:
        return 'A'
    elif score > 0.42:
        return 'B'
    elif score > 0:
        return 'C'
    else:
        return 'D'
    

#if name is main, run the code
if __name__ == '__main__':
    for cluster_name_adjusted in data:
        print(cluster_name_adjusted, get_overall_score(cluster_name_adjusted))