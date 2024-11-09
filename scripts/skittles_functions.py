import pandas as pd
import re
import requests
from bs4 import BeautifulSoup, SoupStrainer
from IPython.core.display import HTML
from io import StringIO
from urllib.request import Request, urlopen




def get_url(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, features = 'html.parser')
    table = str(soup.findAll('table', {'class': 'wikitable'}))

    return table


def get_state_seats(seats, abbrev):
    seats_df = (
        pd
        .read_html(StringIO(str(seats)))[1][['State', 'Total seats']]
        .rename(columns = {'Total seats': 'Districts'})
    )
    abbrev_df = (
        pd
        .read_html(StringIO(str(abbrev)))[1][['Name', 'USPS']]
        .rename(columns = {'Name': 'State', 
                        'Unnamed: 5_level_1': 'Code'})
    )
    state_code_df = pd.merge(seats_df, abbrev_df).droplevel(0, axis=1)
    state_code_df = state_code_df[state_code_df['Code'] != 'NB']
    return state_code_df


def get_states_csv(NUM, ID):
    urls_list = []
    num = 1

    for district, code in zip(NUM, ID):
        while num <= district:
            URL = 'https://www.opensecrets.org/races/summary.csv?cycle=2020&id=' + code + str(num).zfill(2)
            response = requests.get(URL).text
            States_df = pd.read_csv(StringIO(response))
            States_df.insert(0, 'District', str(num).zfill(2))
            col = States_df.pop('State')
            States_df.insert(1, 'State', col)
            urls_list.append(States_df)
            num += 1
        num = 1
       
    States_df = pd.concat(urls_list, ignore_index=True)
    States_csv = States_df.to_csv('../data/States_df.csv', index = False)
   
    return States_csv

