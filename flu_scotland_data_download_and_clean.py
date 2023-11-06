import os
import pandas as pd

def check_data_against_xlsx(xlsx_file, csv_file):
    excel = pd.read_excel(xlsx_file, sheet_name='NHS Health board level', header=9, usecols='A:C')
    csv = pd.read_csv(csv_file)
    return excel, csv

    excel, csv = check_data_against_xlsx('TABLE_1_FLU_HOSPITAL_RAPID_WK_40_2023.xlsx', 'Scotland Respiratory by Health Board.csv')
    influenza_filter = csv.loc[:,'Pathogen'].str.contains('Influenza', case=True)
    week_filter = csv.loc[:,'WeekBeginning']==20231002

    csv.loc[(influenza_filter)&(week_filter)].groupby('HBName')['RatePer100000'].sum()
    return excel, csv

def download_scotland_data():
    data = pd.read_csv('https://www.opendata.nhs.scot/datastore/dump/0cfcbfb1-d659-412f-b699-cddd610679d2?bom=True')
    data.to_csv('Scotland Respiratory by Health Board.csv', index=False)
    print("Scotland Respiratory by Health Board.csv successfully saved")


def rate_to_count_calculation(df, rate, population, factor):
    factor = 100_000

    
def convert_rate_to_count(data):
    population = pd.read_csv('Scotland-mid-year-pop-est-21-data_health_boards.csv')
    
    
    
if __name__ == '__main__':
    # download data
    data = pd.read_csv('https://www.opendata.nhs.scot/datastore/dump/0cfcbfb1-d659-412f-b699-cddd610679d2?bom=True')
    data.to_csv('Scotland Respiratory by Health Board.csv', index=False)
    
    population = pd.read_csv('Scotland-mid-year-pop-est-21-data_health_boards.csv')
    population['All ages'] = population['All ages'].replace(',', '', regex=True).astype(int)

    convert_rate_to_count = pd.merge(left=population,
             right=data,
             how='left',
             left_on='Area code',
             right_on='HB')
        
    convert_rate_to_count['count'] = round(convert_rate_to_count.loc[:,'RatePer100000'].astype(float) * convert_rate_to_count.loc[:,'All ages']/ 100_000).astype(int)
    
    
    convert_rate_to_count.to_csv('scotland_flu_data.csv', index=False)