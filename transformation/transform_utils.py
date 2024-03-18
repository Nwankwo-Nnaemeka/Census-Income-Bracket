import numpy as np
import pandas as pd

def bucketize_with_labels(data, column_name, num_buckets, custom_labels):
    """
     Bcketize a numerical feature with custom labels.

    Args:
        data (pd.DataFrame): The input DataFrame.
        column_name (str): Name of the column to be bucketized.
        num_buckets (int): Number of desired buckets.
        custom_labels (list of str): Custom labels for each bucket.

    Returns:
        pd.Series: A new series with bucket labels.
    """
    # Extract the specified column
    column_values = data[column_name]

    # Use pd.qcut to create quantile-based buckets
    bucketized_series = pd.cut(column_values, bins=num_buckets, labels=custom_labels)

    return bucketized_series

def compute_and_apply_vocabulary(df, column):
    """
    Custom function to compute vocabulary and map words to integer indices.

    Args:
        df (DataFrame): pandas data frame.
        column (str): name of the desired feature.
        

    Returns:
        dict: A dictionary mapping unique words to integer indices.
        series: A Panda series of integers
    """
    # Step 1: Extract all words from the documents
    list_of_words = list(df[column])

    # Step 2: Create a vocabulary dictionary
    vocabulary = {}
    for idx, word in enumerate(set(list_of_words)):
        vocabulary[word] = idx

    # Step 3: Replace words in the documents with their corresponding indices
    
    new_list = df[column].replace(vocabulary)

    return new_list, vocabulary


def min_max_scaler(df, column_name):
    """
    Scales a specific column to the range [0, 1].

    Args:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): Name of the column to be scaled.

    Returns:
        panda.core.series.Series: The DataFrame with the scaled column.
    """
    # Extract the specified column
    column_values = df[column_name].astype('float')

    # Calculate the minimum and maximum values
    min_val = column_values.min()
    max_val = column_values.max()

    # Scale the column to [0, 1]
    scaled_column = (column_values - min_val) / (max_val - min_val)

    return scaled_column
