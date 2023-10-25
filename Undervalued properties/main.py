import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def fetch_property_details(url):
    """Fetches the property details from the provided url."""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        price = soup.find('td',class_='srpTuple__col title_semiBold',  id='srp_tuple_price').text.strip()
    except AttributeError:
        price = np.nan

    try:
        title = soup.find('h2', class_='srpTuple__tupleTitleOverflow').text.strip()
    except AttributeError:
        title = np.nan

    return {'Price': price, 'Property Name': title}

def get_undervalued_properties(url):
    """Gets the list of undervalued properties."""
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    property_list = soup.find_all('div', class_='r_srp__rightSection')
    print(property_list)
    properties = []
    for property in property_list:
        try:
            property_url = 'https://www.99acres.com' + property.find('a')['href']
            property_details = fetch_property_details(property_url)
            property_price = float(property_details['Price'].split(' ')[0].replace(',', ''))

            properties.append({'Property': property_url, 'Property Details': property_details, 'Price': property_price})
        except Exception as e:
            print(f"Error processing property: {e}")
            continue

    return properties

# The base URL of the property listing
base_url = "https://www.99acres.com/property-in-delhi-ncr-ffid"

# The total number of property listings pages
total_pages = 5

# Fetching all undervalued properties from the first 50 pages of property listings
undervalued_properties = []
for i in range(1, total_pages + 1):
    print(f"Processing page {i}")
    properties = get_undervalued_properties(f"{base_url}-{i}")
    undervalued_properties.extend(properties)

# Creating a dataframe from the undervalued properties
df = pd.DataFrame(undervalued_properties)

# Saving the dataframe to a CSV file
df.to_csv('undervalued_properties.csv', index=False)