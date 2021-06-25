import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date', parse_dates=True)
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    sns.lineplot(
    data=df,
    x="date", y="value")
    ax.set(xlabel="Date", ylabel = "Page Views")
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():

    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['month'] = df_bar['date'].dt.month
    df_bar['year'] = df_bar['date'].dt.year
    df_bar.sort_values(by='month',ascending=True,inplace=True)
    
    look_up = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    df_bar['month'] = df_bar['month'].apply(lambda x: look_up[x])

    # Draw bar plot
    fig, ax = plt.subplots()
    sns.barplot(x="year", y="value", hue="month", data=df_bar, ci=None, palette = sns.color_palette()) 
    ax.set(xlabel="Years", ylabel = "Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]

    df_box['month'] = df_box['date'].dt.month
    df_box.sort_values(by='month',ascending=True,inplace=True)
    
    look_up = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

    df_box['month'] = df_box['month'].apply(lambda y: look_up[y])

    #print(df_box['month'])

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(ncols=2)
    sns.boxplot(x="year", y="value", data=df_box, width = 0.6, ax=axs[0]).set_title("Year-wise Box Plot (Trend)")
    axs[0].set(xlabel="Year", ylabel = "Page Views")
    sns.boxplot(x="month", y="value", data=df_box, width = 0.6, ax=axs[1]).set_title("Month-wise Box Plot (Seasonality)")
    axs[1].set(xlabel="Month", ylabel = "Page Views")
    # Save image and return fig (don't change this part)
    fig.tight_layout(pad=3.0)
    #plt.xticks(rotation=90)
    fig.savefig('box_plot.png')
    
    
    return fig
