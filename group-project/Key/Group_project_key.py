# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 10:57:13 2025

@author: Prof Anderson

Key for group assignmnet
"""

# Import libraries 
import numpy as np
import pandas as pd
from scipy import stats 
import random


""" Question 2A """ # =============================================================================

# Import GED dataset
path = r"C:\Users\nicho\OneDrive\Desktop\MDS\QMSS-GR5072-Spring2025\Week 5\Activity"
df = pd.read_csv(path + r"\3 ged_data.csv")

# Modify t_test() function from week 5 activity
def t_test(data, num_vars, bin_vars):
    """
    Computes an independent two-sample t-test for the difference in means between two groups for each combination of continuous and binary variables.

    Args:
        num_vars: A list of numeric variable names.
        bin_vars: A list binary variable names. All binary variables must be 
            dichotomous (i.e., have exactly two unique values).

    Returns:
        A pandas DataFrame with the following columns for each combination of numerical and binary variables:
        - "Continuous Variable": the name of the numerical variable
        - "Binary Variable": the name of the binary variable
        - "Total Sample Size": the total sample size of the two groups combined
        - "Mean Difference": the difference in means between the two groups
        - "SE of Mean Difference": the standard error of the mean difference
        - "DF": the degrees of freedom
        - "t-statistic": the t-statistic
        - "P-value": the two-tailed p-value

    Raises:
        AssertionError: If any binary variable in bin_vars is not dichotomous.
    """
    
    # Check that all bin_vars elements are binary
    for bin_var in data[bin_vars]:
        assert np.unique(data[bin_var]).shape == (2,), "All bin_vars must be dichotomus!"
     
    # Combine data
    data = data[num_vars + bin_vars]
    
    results = []
    
    for i, num_var in enumerate(num_vars):
        for j, bin_var in enumerate(bin_vars):
            
            # Get the unique values of the binary variable
            unique_vals = np.unique(data[bin_var])
            
            # Calculate the mean difference between the two groups
            group1 = data[num_var][data[bin_var] == unique_vals[0]]
            group2 = data[num_var][data[bin_var] == unique_vals[1]]
            mean_diff = group2.mean() - group1.mean()
            
            # Calculate the sample sizes and sample variances of the two groups
            n1 = group1.shape[0]
            n2 = group2.shape[0]
            s1 = group1.var()
            s2 = group2.var()
            
            # Calculate the degrees of freedom (DF)
            DF = n1 + n2 - 2
            
            # Calculate the pooled standard deviation (sp)
            sp = np.sqrt(((n1 - 1) * (s1**2) + (n2 - 1) * (s2**2)) / DF)
            
            # Calculate the standard error of the mean difference
            SE_mean_diff = sp * np.sqrt(1/n1 + 1/n2)
            
            # Calculate the t-statistic
            t_statistic = mean_diff / SE_mean_diff
            
            # Calculate the p-value
            p_value = 2 * (1 - stats.t.cdf(np.abs(t_statistic), DF))
            
            # Append the results to the results list
            results.append({
                "Continuous Variable": num_var,
                "Binary Variable": bin_var,
                "Total Sample Size": n1 + n2,
                "Mean Difference": round(mean_diff, 2), 
                "SE of Mean Difference": round(SE_mean_diff, 2),
                "DF": DF,
                "t-statistic": round(t_statistic, 3),
                "P-value": format(p_value, ".3f")
            })
    
    # Convert the results list to a DataFrame
    return pd.DataFrame(results)

""" Question 2B """ 

?t_test


""" Question 2C """ 

# Recode the GED variable
df["ged_cats"] = np.where(df["ged"] == 1, "ged", "no ged")

# Call the t_test function
results = t_test(data=df, num_vars=["income_log", "post_sec_edu"], bin_vars=["ged","ged_cats","female"])
results


""" Question 2D """ 

# Test a categorical variable with 3+ categories
results = t_test(data=df, num_vars=["income_log", "post_sec_edu"], bin_vars=["ged", "BYRACE"])
results


""" Question 3 """ # =============================================================================

def simulate_race():
    # Set up initial positions
    t_position = 1
    h_position = 1

    # Define the range of positions
    positions = list(range(1, 71))

    # Define the moves of the tortoise and hare
    tortoise_moves = {
        "Fast Pod": 3,
        "Slip": -6,
        "Slow Pod": 1
    }
    hare_moves = {
        "Sleep": 0,
        "Big Hop": 9,
        "Big Slip": -12,
        "Small Hop": 1,
        "Small Slip": -2
    }

    # Print the starting message
    print("BANG ! ! ! !")
    print("AND THEY'RE OFF ! ! ! !")

    # Loop until one of the animals wins or there is a tie
    while t_position < 70 and h_position < 70:
        # Move the tortoise
        t_move = random.randint(1, 10)
        if t_move <= 5:
            t_position += tortoise_moves["Fast Pod"]
        elif t_move <= 7:
            t_position += tortoise_moves["Slip"]
        else:
            t_position += tortoise_moves["Slow Pod"]

        # Move the hare
        h_move = random.randint(1, 10)
        if h_move <= 2:
            h_position += hare_moves["Sleep"]
        elif h_move <= 4:
            h_position += hare_moves["Big Hop"]
        elif h_move <= 5:
            h_position += hare_moves["Big Slip"]
        elif h_move <= 8:
            h_position += hare_moves["Small Hop"]
        else:
            h_position += hare_moves["Small Slip"]

        # Adjust positions if out of range
        if t_position < 1:
            t_position = 1
        if h_position < 1:
            h_position = 1
        if t_position > 70:
            t_position = 70
        if h_position > 70:
            h_position = 70

        # Print the current position
        race_line = [" "] * 70
        if t_position == h_position:
            race_line[t_position-1] = "OUCH!!!"
            race_line[-7] = "|"
        elif t_position == 1:
            race_line[-1] = "|"
            race_line[h_position-1] = "H"
        elif h_position == 1:
            race_line[-1] = "|"
            race_line[t_position-1] = "T"
        else:
            race_line[t_position-1] = "T"
            race_line[h_position-1] = "H"
            race_line[-1] = "|"
        race_line[0] = "_"
        print("".join(race_line))

        # Check if either animal has won
        if t_position >= 70 and h_position < 70:
            print("TORTOISE WINS!!! YAY!!!")
        elif h_position >= 70 and t_position < 70:
            print("Hare wins. Yawn. . .")
        elif t_position >= 70 and h_position >= 70:
            print("It's a tie.")
        else:
            continue
        break

# Simulate race!
simulate_race()


""" Question 4A """ # =============================================================================

# Import data
path = r"C:\Users\nicho\OneDrive\Desktop\MDS\QMSS-GR5072-Spring2025-HWs\group-project\Data"
df = pd.read_csv(path + r"\Employee_census_data.csv")
df

# Calculate soc (# of direct reports) for all supervisors. Merge in, filling in zeros as neccessary
df1 = df.groupby('supid').size().reset_index(name='soc') \
        .rename(columns={'supid': 'eeid'}) \
        .merge(df, on='eeid', how='right') \
        .fillna({'soc': 0}) \
        .filter(['eeid', 'supid', 'grade', 'soc']) \
        .sort_values(by='soc', ascending=False) 
df1['supervisor'] = np.where(df1['soc'] > 0, 1, 0)  # Var created here but needs to be updated below
df1
pd.crosstab(index=df1['soc'], columns=df1['supervisor']) # Check answer

""" Question 4B """ 

# Create calc_soc_total() function
#   Starting from the lowest level and advancing up one level at a time, take their direct reports 
#   and add this to their supervisor's total. Repeat until we've gone through all levels.

def calc_soc_total(data):
    global level # Save level to the global environment as we update it with each call of this function    
    
    if level <= max_level:
        df_ = data[data['grade'] == level] \
                .groupby('supid')['soc_total'].sum().reset_index(name='soc_total_') \
                .rename(columns={'supid': 'eeid'}) \
                .merge(data, on='eeid', how='right') \
                .fillna({'soc_total_': 0}) \
                .assign(soc_total=lambda x: x['soc_total'] + x['soc_total_']) \
                .filter(['eeid', 'supid', 'grade', 'soc', 'supervisor', 'soc_total']) \
                .sort_values(by='soc_total', ascending = False)
        
        level += 1
        return calc_soc_total(df_)
    
    else:
        return data.sort_values(by='grade', ascending = False)
        
# Set parameters before running function
level = 1  # Start at lowest org level
max_level = np.max(df1['grade']) - 1 # Minus 1 bc each step compares the lower level to a higher level
df1['soc_total'] = df1['soc'] # Var created here but is updated in the function call below

# Run function and check answer
final_df = calc_soc_total(df1)
final_df 

# Export data
final_df.to_csv(r"C:\Users\nicho\OneDrive\Desktop\MDS\QMSS-GR5072-Spring2025-HWs\group-project\key\Q4 solution data.csv")

