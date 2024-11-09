import pandas as pd
import re
import matplotlib.pyplot as plt
import requests
import plotly.express as px
from bs4 import BeautifulSoup, SoupStrainer
from IPython.core.display import HTML
from io import StringIO
from urllib.request import Request, urlopen
import glob


def state_code_df():
    wiki_abbrev_url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations'
    r_abbrev = requests.get(wiki_abbrev_url)
    soup_abbrev = BeautifulSoup(r_abbrev.text, features = 'html.parser')
    abbrev_table = str(soup_abbrev.findAll('table', {'class': 'wikitable'}))
    abbrev_df = (
        pd
        .read_html(StringIO(str(abbrev_table)))[1][['Name', 'USPS']]
        .rename(columns = {'Name': 'State', 
                           'Unnamed: 5_level_1': 'Code'})
    )
    wiki_district_url = 'https://en.wikipedia.org/wiki/2020_United_States_House_of_Representatives_elections'
    r_district = requests.get(wiki_district_url)
    soup_district = BeautifulSoup(r_district.text, features = 'html.parser')
    district_table = str(soup_district.findAll('table', {'class': 'wikitable'}))
    seats_df = (
        pd
        .read_html(StringIO(str(district_table)))[1][['State', 'Total seats']]
        .rename(columns = {'Total seats': 'Districts'})
    )
    state_code_df = pd.merge(seats_df, abbrev_df).droplevel(0, axis=1)
    state_code_df = state_code_df[state_code_df['Code'] != 'NB']
    NUM = state_code_df['Districts'].tolist()
    ID = state_code_df['Code'].tolist()
    return NUM, ID


def get_tn_districts():
    TN07_URL = 'https://www.opensecrets.org/races/summary.csv?cycle=2020&id=TN07'
    response = requests.get(TN07_URL).text
    TN07_df = pd.read_csv(StringIO(response))
    urls_list = []
    num = 1
    while num < 10:
        URL = 'https://www.opensecrets.org/races/summary.csv?cycle=2020&id=TN' + str(num).zfill(2)
        response = requests.get(URL).text
        TN_df = pd.read_csv(StringIO(response))
        TN_df.insert(0, 'District', str(num).zfill(2))
        urls_list.append(TN_df)
        num += 1
    TN_df = pd.concat(urls_list)
    return TN_df


def get_all_districts():
    urls_list = []
    num = 1
    NUM, ID = state_code_df()
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
    States_df['Party'] = States_df['FirstLastP'].str.split(' ').str[-1]
    return States_df