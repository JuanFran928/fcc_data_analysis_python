import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create Scatter plot
    # Previously I tried the folowing code:
    # plt.figure(figsize=(12,8))
    # ax = plt.scatter(x='Year', y='CSIRO Adjusted Sea Level')

    # Start off with X-axis and Y-axis as below
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.scatter(x,y)


# Create FIRST line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # First grab the current Slope & Intercept values
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    # Using the above Slope/ Intercept values now plot Best Fit 1
    x1 = list(range(1880, 2050)) 
    y1 = []

    for year in x1:
      y1.append(intercept + slope * year)

    plt.plot(x1, y1, 'r', label = 'Best Fit Line 1')
    plt.legend()
    # plt.show()
    
    # Create Second line of Best fit
    # SECOND best fit for year 2000 onwards so shall have new slope and intercept

    xfuture = df[df['Year'] >= 2000] ['Year']
    yfuture = df[df['Year'] >= 2000] ['CSIRO Adjusted Sea Level']

    newfit = linregress(xfuture, yfuture)
    newslope = newfit.slope
    newintercept = newfit.intercept

    xfuture2 = list(range(2000, 2050))
    yfuture2 = []

    for xfuture in xfuture2:
      yfuture2.append(newintercept + newslope * xfuture)
        
    plt.plot(xfuture2, yfuture2, 'r', label = 'Best Fit Line 2', color='green')
    plt.legend()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
