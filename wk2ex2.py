# import required libraries to your workspace

import pandas as pd

import matplotlib.pyplot as plt

def sales_plot(filename, index_column):
    # read the csv file using pandas and copy the resulting dataframe to variable df
    df = pd.read_csv(filename, index_col= index_column)

    # examine the dataframe df
    print(df.head())
    
    print(df.info())
    print("The shape is " + str(df.shape))
    print("columns names are:  " + str(df.columns))

    #To create a simple plot
    df.plot()

    plt.show()

    plt.savefig('adsales_lineplot.png')