import pandas as pd
import requests
from bs4 import BeautifulSoup


def parse_data(webpage):
    data = requests.get(url=webpage)
    data_soup = BeautifulSoup(data.content, 'html.parser')
    return data_soup


def iterate_through_divs_once(data_soup):
    for result in data_soup.find_all("div"):
        return result.find_all("div")
    

## doesnt really work as the result returns a list, not string
# def iterate_through_divs_n_times(data_soup, n):
#     result = iterate_through_divs_once(data_soup)
    
#     for i in range(n):
#         result = iterate_through_divs_once(result)
        
#     return result


def retrieve_line_with_url(webpage):
    # return data_soup
    data_soup = parse_data(webpage)

    for a in data_soup.find_all("div"):
        for b in a.find_all("div"):
            for c in b.find_all("div"):
                for d in c.find_all("div"):
                    for e in d.find_all("div"):
                        for f in e.find_all("div"):
                          for g in f.find_all("a"):
                        
                            print(g)
                            

def retrieve_href(webpage, text_in_url):
    # return data_soup
    data_soup = parse_data(webpage)

    for a in data_soup.find_all("div"):
        for b in a.find_all("div"):
            for c in b.find_all("div"):
                for d in c.find_all("div"):
                    for e in d.find_all("div"):
                        for f in e.find_all("div"):
                          for g in f.find_all("a"):
                        
                            # print(g)         
                            # print(g['href'])
                            
                            # Retrieve the first URL with the text bellow
                            if g['href'].find(text_in_url) >-1 : 
                                # Use this link to scrape
                                linkToScrape = g['href']
                                return linkToScrape


url = "https://www.opendatani.gov.uk/@public-health-agency/notification-of-infectious-diseases"
data_soup = parse_data(url)