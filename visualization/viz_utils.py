import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def plot(data, column, hues= "income"):
    """
    Args:
        data (pd.DataFrame): the data frame to be used for the plot
        column (str): name of feature to be ploted on the x axis
        hues (str, optional): name of feature to used to assign colors to each category if not 
        then y label is used in this case income
    Returns:
        None
        
    """
    plt.figure(figsize=(10,5))
    ax = sns.countplot(data, x=column, hue = hues, edgecolor = 'k', palette = 'Set2')
    plt.xticks(rotation=90)
    ax.set_title(f"{column.title()} / {hues.title()}")
    ax.set_xlabel(f"{column.title()}")
    plt.show()


def num_plot(data, column, label = "income"):
    
    """
    Args:
        data (pd.DataFrame): the data frame to be used for the plot
        column (str): name of feature to be plotted on the x-axis
        hues (str, optional): name of the feature to be used to assign colors to each category if not 
        then y label is used in this case income
    Returns:
        None
        
    """

    plt.figure(figsize=(10,5))
    ax = sns.FacetGrid(data, row=label, margin_titles=True, aspect=4, height=3)
    ax.map(plt.hist, column, bins= 100)
    plt.show()
