import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 9))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points')

    # Create first line of best fit
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_predict = range(1880, 2051)
    y_predict = reg1.slope * x_predict + reg1.intercept
    plt.plot(x_predict, y_predict, c='c', label='Best Fit Line')
    plt.xlabel('Year')
    plt.ylabel('Sea Level')
    plt.title('')
    plt.legend()

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()