import pandas as pd


if __name__ == '__main__':
    # download data
    
    data = pd.read_csv('https://www.opendata.nhs.scot/datastore/dump/0cfcbfb1-d659-412f-b699-cddd610679d2?bom=True')
    data.to_csv('Scotland Respiratory by Health Board.csv', index=False)
