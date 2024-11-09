import pandas as pd 
import io
import re 
import requests 
from bs4 import BeautifulSoup
from io import StringIO
from IPython.core.display import HTML
import plotly.express as px 
import glob
import os

def get_url_text(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, features = 'html.parser')
    return soup


def get_wiki_table(url):
    wiki_response = requests.get(url).text
    wiki_soup = BeautifulSoup(wiki_response, features = 'html.parser')
    wiki_tables = wiki_soup.findAll('table', {'class':'wikitable'})
    return wiki_tables


def convert_wikitable_to_df(wiki_table, table_index):
    wikitable_df = pd.read_html(StringIO(str(wiki_table)))[table_index]
    return wikitable_df


def get_districts_df(url, districts, initials):
    urls_list = []
    num = 1
    for district, state_initial in zip(districts, initials):
        while num <= district:
            state_district_url = url + state_initial + str(num).zfill(2)
            response = requests.get(state_district_url).text
            states_df = pd.read_csv(StringIO(response))
            states_df.insert(0, 'District', str(num).zfill(2))
            states_col = states_df.pop('State')
            states_df.insert(1, 'State', states_col)
            urls_list.append(states_df)
            num += 1
        num = 1
    states_df = pd.concat(urls_list, ignore_index=True)
    return states_df