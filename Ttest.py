'''
T-test: general concepts

1. Find t-value: signal/noise --> |mean1 - mean2|/ sq((SD1^2/count1) + (SD2^2/count2)) 
    - create a mean calculator
    - create a standard deviation calcular
    - find the count of the two sets of data
    - if t-value > 1 --> there is more signal ; if t-value < 1 --> there is more noise 

2. Use a p-value table to find if we reject or accept null hypothesis
    - Calculate the degrees of freedom : df = (count1 - 1 ) + (count2 - 1)
    - Determine p-value using df
    - if t-value is HIGHER than p-value --> reject ; if t-value is LOWER than p-value --> accept

3. Include a parameter for one-tailed vs two-tailed, paired or not (array1, array2, type)
    - Tails --> determines the difference in one or two directions
        - 1: one-tailed, 2: two-tailed (in both cases variance in not equal)
    - Type --> if the dataset is from the same field of different (if paired/from the same field, they must have the same count)
        - 1: paired, 2: one-sample T-test, 3(default): independent

'''

import numpy as np
from scipy import stats
import pandas as pd

excel_path = r'C:\Users\anish\OneDrive\Documents\Basic Stat For Research\ExampleDataForTtest.xlsx'
df1 = pd.read_excel(excel_path, sheet_name = 1, usecols = 'D', skiprows = 1, nrows = None, engine='openpyxl') # sheet count starts at 0
df2 = pd.read_excel(excel_path, sheet_name = 1, usecols = 'C', skiprows = 1, nrows = None, engine='openpyxl')

data1 = df1.values.flatten() # changes to a 1D array
data2 = df2.values.flatten()

def ttest(data1, data2, type = 3):
    alpha = 0.05
    a = []

    if type == 1: # paired T-test 
        x = input("One-tailed(1) or Two-tailed(2): ")
        x = int(x)
        if x == 1: # if one-tailed, paired
            y = input("Is the first set 'less' or 'greater' than second set: ")
            t_statistic, p_value = stats.ttest_rel(data1, data2, alternative = y)
            alpha = alpha/2
        else: # if two-tailed, paired 
            t_statistic, p_value = stats.ttest_rel(data1, data2)
    
    if type == 2: # one-sample T-test                                                     
        z = input("One-tailed(1) or Two-tailed(2): ")
        z = int(z)
        x = input("what is the known mean value: ")
        y = input("what dataset are we comparing (1 or 2): ")
        y = int(y)

        if y == 1:
            a = data1
        elif y == 2:
            a = data2
        
        mean = np.round(float(x), decimals=4)
        t_statistic, p_value = stats.ttest_1samp(a, mean) # (a=data array, mean=known mean)

        if z == 1: # if one-tailed, one-sample 
            alpha = alpha/2

    if type == 3: # default: two independent datasets T-test 
        x = input("One-tailed(1) or Two-tailed(2): ")
        x = int(x)
        y = input("Assuming equal variances? (t/f): ")
        
        if y == 't':
            t_statistic, p_value = stats.ttest_ind(data1, data2, equal_var=True)
        else:
            t_statistic, p_value = stats.ttest_ind(data1, data2, equal_var=False)
        
            
        if x == 1: # one-tailed
           p_value = p_value/2

    
    print("t-statistic:", np.round((np.abs(t_statistic)), decimals = 5))
    print("p-value:", np.round(p_value, decimals = 7))

    if p_value < alpha:
        result = print("Reject Ho: there is significant difference")
    else:
        result = print("Don't Reject Ho: NO significant difference")

    return result

x = ttest(data1, data2)





