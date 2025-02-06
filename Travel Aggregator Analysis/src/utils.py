import pandas as pd
import numpy as np

def missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """Check for missing values in a DataFrame"""
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input must be a Pandas DataFrame")
    
    missing = data.isnull().sum().sort_values(ascending=False)
    missing_percentage = np.round((data.isnull().sum().sort_values(ascending=False) / len(data)), 2)

    missing_df =  pd.DataFrame({
        'column': missing.index,
        'count': missing.values, 
        '%' : missing_percentage.values
    })

    return missing_df[missing_df['count'] > 0]