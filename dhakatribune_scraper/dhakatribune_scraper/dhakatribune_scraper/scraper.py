import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

def scraper_code_with_no_headers():
    check_dir()
    check_files()
    
    df = pd.read_csv('scrapped_data/data.csv', header=None, skiprows=1)
    df.columns = ["URL", "Category"]

    tqdm.pandas(desc="Scraping URLs")
    df['Title'], df['Body'] = zip(*df['URL'].progress_apply(revised_extract_content))

    for category, group_df in df.groupby('Category'):
        group_df.drop('Category', axis=1).to_csv(f"scrapped_data/{category}.csv", index=False)

    return "Scraping and saving completed without headers."

def revised_extract_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        title = soup.select_one('.title.mb10')
        title = title.text.strip() if title else None
        body = soup.select_one('article.jw_detail_content_holder.jw_detail_content_body.content.mb16')
        body = body.text.strip() if body else None
        return title, body
    except Exception as e:
        print(f"Error fetching data for URL {url}: {e}")
        return None, None

def check_files():
    if os.path.exists('scrapped_data/data.csv'):
        with open('scrapped_data/data.csv', 'r', encoding='utf-8') as f, \
             open('scrapped_data/data_bak.csv', 'w', encoding='utf-8') as f1:
            for line in f:
                f1.write(line)
        print('your file has been backed up to scrapped_data/data_bak.csv')
    else:
        with open('scrapped_data/data.csv', 'w', encoding='utf-8') as f:
            f.write('URL,Category\\n')

def check_dir():
    os.makedirs('scrapped_data', exist_ok=True)
