import os
import pandas as pd
import time

def check_data_against_xlsx(xlsx_file, csv_file):
    excel = pd.read_excel(xlsx_file, sheet_name='NHS Health board level', header=9, usecols='A:C')
    csv = pd.read_csv(csv_file)
    return excel, csv

    excel, csv = check_data_against_xlsx('TABLE_1_FLU_HOSPITAL_RAPID_WK_40_2023.xlsx', 'Scotland Respiratory by Health Board.csv')
    influenza_filter = csv.loc[:,'Pathogen'].str.contains('Influenza', case=True)
    week_filter = csv.loc[:,'WeekBeginning']==20231002

    csv.loc[(influenza_filter)&(week_filter)].groupby('HBName')['RatePer100000'].sum()
    return excel, csv

    
if __name__ == '__main__':
    # download data
    
    data = pd.read_csv('https://www.opendata.nhs.scot/datastore/dump/0cfcbfb1-d659-412f-b699-cddd610679d2?bom=True')
    data.to_csv('Scotland Respiratory by Health Board.csv', index=False)
    
