import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize an empty list to store the data
data_list = []

# Specify the base URL of the books you want to scrape
base_url = "https://www.goodreads.com/book/show/"
book_ids = ['55196813', '58468990', '60194162', '63241097', '62549616',
            '55146813', '58748990', '65194162', '63141097', '52589616']

# Loop through the list of book IDs
for book_id in book_ids:
    # Construct the URL for the book
    url = f'{base_url}{book_id}'

    # Send an HTTP request to the URL and parse the HTML content of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements containing the desired information using the appropriate CSS selectors or XPaths

    # Find the title, if available, otherwise set to 'Title not found'
    title_element = soup.find('h1')
    title = title_element.text if title_element else 'Title not found'

    # Check if the author element exists before accessing its text attribute
    author_element = soup.find('span', {'class': 'ContributorLink__name'})
    author = author_element.text if author_element else 'Author not found'

    # Find the book description, if available, otherwise set to 'Description not found'
    description_element = soup.find('span', {'class': 'Formatted'})
    description = description_element.text if description_element else 'Description not found'

    # Find the published date, if available, otherwise set to 'Published Date not found'
    published_date_element = soup.find('p', {'data-testid': 'publicationInfo'})
    published_date = published_date_element.text.split(' ', 2)[-1] if published_date_element else 'Published Date not found'

    # Store the scraped data in a dictionary
    data = {'Title': title, 'Author': author, 'Published_Date': published_date, 'Description': description}
    data_list.append(data)

    # Adding a delay to avoid overloading the website's server
    #time.sleep(2)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Save the data to an Excel file
df.to_excel('authors_data.xlsx', index=False)

# Print the DataFrame to verify the scraped data
print(df)
