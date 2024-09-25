import pandas as pd

def read_csv():
    # Load the data
    df = pd.read_csv('data/zombie-data.csv')

    # Print the DataFrame
    print(df.head())

def main():
    read_csv()

if __name__ == "__main__":
    main()
