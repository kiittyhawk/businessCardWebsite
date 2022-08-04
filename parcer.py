import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re


def get_titles():
    URL_TEMPLATE = "https://vk.com/cloudyvape"
    r = requests.get(URL_TEMPLATE)

    titles = []

    soup = bs(r.text, "html.parser")
    quotes = soup.find_all('div', class_='pi_text')
    for name in quotes:
        titles.append(name.span)
    return titles

def remove_symbols(str):
    if str[0] == '!' or str[0] == '.' or str[0] == '?':
        str = str.replace(str[0], '')
    return str

def get_part(title):
    arr = []
    num = 0
    key = ''
    val = ''
    
    i = 0
    while i < len(title):
        if title[i] == '.' or title[i] == '!' or title[i] == '?':
            arr.append(i)
        i += 1
    i = 0
    while i < len(arr):
        if arr[i] > num and arr[i] < 70:
            num = arr[i]
        # print(arr)
        i += 1
    i = 0
    while i <= num:
        key += title[i]
        i += 1
    i = 0
    while num < len(title):
        val += title[num]
        num += 1
        i += 1
    return {remove_symbols(key): remove_symbols(val)}    

def parcer(arr):
    titles = {}
    for title in arr:
        title = re.sub(r'\<[^>]*\>', '', str(title))
        if len(title) <= 40:
            part = {title: ''}
            titles.update(part)
        else:
            part = get_part(title)
            titles.update(part)

    print(titles)
if __name__ == "__main__":
    titles = get_titles()
    parcer(titles)
