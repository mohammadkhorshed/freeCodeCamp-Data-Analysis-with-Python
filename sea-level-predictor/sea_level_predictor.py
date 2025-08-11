import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 9))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points')

    # Create first line of best fit
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = range(1880, 2051)
    y_pred1 = reg1.slope * x_pred1 + reg1.intercept
    plt.plot(x_pred1, y_pred1, c='c', label='Best Fit Line (1880-2013)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]

    reg2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = range(2000, 2051)
    y_pred2 = reg1.slope * x_pred2 + reg1.intercept
    plt.plot(x_pred2, y_pred2, c='r', label='Best Fit Line (2000-2013)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea-level-predictor/sea_level_plot.png')
    return plt.gca()