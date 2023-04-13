import pandas as pd
from scipy import stats
import numpy as np

def explanatory_analysis(charges_data_path, personal_data_path, plan_data_path):
    # Read in all three datasets
    charges_data = pd.read_csv(charges_data_path)
    personal_data = pd.read_csv(personal_data_path)
    plan_data = pd.read_csv(plan_data_path)
    
    # Fill in missing values in monthlyCharges column with trimmed mean
    non_missing = charges_data.monthlyCharges[charges_data.monthlyCharges.notnull()]
    avg_trimmed = non_missing[(non_missing >= non_missing.quantile(0.1)) &
                              (non_missing <= non_missing.quantile(0.9))].mean()
    monthly_charges_mean = round(avg_trimmed)
    charges_data.monthlyCharges.fillna(monthly_charges_mean, inplace=True)

    
    # Fill in missing values in totalCharges column
    charges_data['totalCharges'] = charges_data['totalCharges'].fillna(charges_data['monthlyCharges'] * charges_data['tenure'])
    
    # Create tenureBinned column by discretizing tenure
    bins = [0, 24, 48, 60, np.inf]
    labels = ['group1', 'group2', 'group3', 'group4']
    charges_data['tenureBinned'] = pd.cut(charges_data['tenure'], bins=bins, labels=labels)
    
    # Calculate churn rate
    churn_rate = (charges_data['churn'].value_counts(normalize=True)['Yes'] * 100).round()
    
    # Join charges_data with personal_data by customerID
    merged_data = pd.merge(charges_data, personal_data, on='customerID', how='inner')
    
    # Join merged_data with plan_data by customerID
    merged_data = pd.merge(merged_data, plan_data, on='customerID', how='left')
    
    # Calculate percentage of customers older than 60
    age_above_60_pct = ((merged_data['age'] > 60).sum() / len(merged_data) * 100).round()
    
    # Create dictionary of internetService value counts
    internet_service_counts = merged_data['internetService'].value_counts().to_dict()
    
    # Return dictionary of calculated values
    results = {
        'monthly_charges_mean': int(charges_data['monthlyCharges'].mean()),
        'charges_data_updated': charges_data,
        'churn_pct': int(churn_rate),
        'data_merged': merged_data,
        'pct_age_above_60': int(age_above_60_pct),
        'internet_service_counts': internet_service_counts
    }
    return results
