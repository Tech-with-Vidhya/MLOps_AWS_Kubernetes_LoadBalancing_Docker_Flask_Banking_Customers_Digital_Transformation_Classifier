
import pandas as pd

# Function to read the data file 
def read_data(file_path, **kwargs):
    raw_data = pd.read_csv(file_path  ,**kwargs)
    return raw_data


# Function to merge different data files 
def merge_dataset(df1, df2, join_type, on_param):
    final_df = df1.copy()
    final_df = final_df.merge(df2, how=join_type, on=on_param)
    return final_df


# Function to drop columns from data
def drop_col(df, col_list):
    for col in col_list:
        if col not in df.columns:
            raise ValueError(
                f"Column does not exit in dataframe")
        else: 
            df = df.drop(col, axis=1)
    return(df)


# Function to remove null values
def null_values(df):
    df = df.dropna()
    return df


# Function to find maximum value and returning maximum value and its index
def max_val_index(l):
    max_l = max(l)
    max_index = l.index(max_l)
    return (max_l, max_index)