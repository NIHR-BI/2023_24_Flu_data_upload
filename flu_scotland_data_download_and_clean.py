import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def check_data_against_xlsx(xlsx_file, csv_file):
    excel = pd.read_excel(xlsx_file, sheet_name='NHS Health board level', header=9, usecols='A:C')
    csv = pd.read_csv(csv_file)
    return excel, csv

    excel, csv = check_data_against_xlsx('TABLE_1_FLU_HOSPITAL_RAPID_WK_40_2023.xlsx', 'Scotland Respiratory by Health Board.csv')
    influenza_filter = csv.loc[:,'Pathogen'].str.contains('Influenza', case=True)
    week_filter = csv.loc[:,'WeekBeginning']==20231002

    csv.loc[(influenza_filter)&(week_filter)].groupby('HBName')['RatePer100000'].sum()
    return excel, csv
   
    
def startWebDriver():
    global driver
    options = Options()
    options.add_argument('--headless')
    # options.headless = True
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    
    
def enable_download_in_headless_chrome(browser, download_dir):
    #add missing support for chrome "send_command"  to selenium webdriver
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


def run_test_selenium_click():
    startWebDriver()
    enable_download_in_headless_chrome(driver, os.getcwd())
    driver.get('https://scotland.shinyapps.io/phs-respiratory-covid-19/')
    time.sleep(7)
    # # click download data
    download_data_tab = driver.find_element('xpath', '//*[@id="jump_to_download"]')
    download_data_tab.click()
    time.sleep(3)

    # driver.quit()
    from selenium.webdriver.common.by import By
    # # click radio button respiratory infection activity twice so that it is reg
    radio_button_resp_infection = driver.find_element(By.XPATH, '//*[@id="download_indicator"]/div/label[4]/input')
    radio_button_resp_infection.click()
    time.sleep(7)
    
    # # click download data. the first one saves historic radio button
    download_data_button = driver.find_element('xpath', '//*[@id="data_download_output"]')
    download_data_button.click()
    driver.quit()
    
    
if __name__ == '__main__':
    # download data
    
    data = pd.read_csv('https://www.opendata.nhs.scot/datastore/dump/0cfcbfb1-d659-412f-b699-cddd610679d2?bom=True')
    data.to_csv('Scotland Respiratory by Health Board.csv', index=False)

    run_test_selenium_click()
