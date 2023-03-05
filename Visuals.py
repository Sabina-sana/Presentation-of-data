import pandas as pd
import matplotlib.pyplot as plt

def PieGraph():
    ''' 
    to create a pie chart showing the total sales for each region (NA, EU, JP, Other) and for the global total.
    '''
    df = pd.read_csv('vgsales.csv')
    
    # Calculate the total sales for each region
    na_sales = df['NA_Sales'].sum()
    eu_sales = df['EU_Sales'].sum()
    jp_sales = df['JP_Sales'].sum()
    other_sales = df['Other_Sales'].sum()
    global_sales = df['Global_Sales'].sum()

    # Create a pie chart
    labels = ['NA', 'EU', 'JP', 'Other', 'Global']
    values = [na_sales, eu_sales, jp_sales, other_sales, global_sales]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Global Video Game Sales by Region")
    plt.show()
    


def BarGraph():
    ''' 
    to create a bar chart showing the top 10 publishers by total global sales.
    '''
    # Load the dataset
    df = pd.read_csv('vgsales.csv')
    # Group the data by publisher and calculate the total sales for each publisher
    publisher_sales = df.groupby('Publisher')['Global_Sales'].sum()

    # Sort the publishers by total sales in descending order
    publisher_sales = publisher_sales.sort_values(ascending=False)

    # Create a bar chart showing the top 10 publishers by total sales
    top_publishers = publisher_sales.head(10)
    # fig size
    fig, ax = plt.subplots(figsize=(5,5))

    ax.bar(top_publishers.index, top_publishers.values)
    ax.set_title("Top Publishers by Global Sales")
    ax.set_xlabel("Publisher")
    ax.set_ylabel("Total Sales (millions of units)")
    plt.xticks(rotation=800)
    plt.show()
    

def LineGraph():
    ''' 
    to create a line chart showing the sales of the top 3 publishers over time.
    '''
    # Select the top 3 publishers and create a line chart showing their sales over time
    # Load the dataset
    df = pd.read_csv('vgsales.csv')
    # Group the data by publisher and calculate the total sales for each publisher
    publisher_sales = df.groupby('Publisher')['Global_Sales'].sum()

    # Sort the publishers by total sales in descending order
    publisher_sales = publisher_sales.sort_values(ascending=False)
    top_3_publishers = publisher_sales.head(3)
    df_top_3 = df[df['Publisher'].isin(top_3_publishers.index)]
    df_top_3 = df_top_3.groupby(['Publisher', 'Year'])['Global_Sales'].sum().reset_index()

    fig, ax = plt.subplots()
    for publisher in top_3_publishers.index:
        publisher_data = df_top_3[df_top_3['Publisher'] == publisher]
        ax.plot(publisher_data['Year'], publisher_data['Global_Sales'], label=publisher)
    ax.set_title("Top 3 Publishers' Global Sales over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Sales (millions of units)")
    plt.legend()
    plt.show()
    

def main():
    LineGraph().__doc__
    BarGraph().__doc__
    PieGraph().__doc__

if __name__ == "__main__":
    main()