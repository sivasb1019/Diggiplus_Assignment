# Web scraping on a real estate website, specifically "99acres.com" which fetches information about property listings, identifies undervalued properties, and saves the data into a CSV file. 

### 1. Importing Libraries:

* The script starts by importing the required Python libraries, including requests, BeautifulSoup from the bs4 module (for web scraping), pandas and numpy(for data manipulation and storage), and time.
* Install the required librarires before running the "main.py" using "requirements.txt" file or install manually.
### 2. fetch_property_details(url) Function:

* This function takes a URL as input and fetches details about a specific property.
* It sends an HTTP request to the provided URL with a user-agent header to simulate a web browser request.
* The HTML content of the page is parsed using BeautifulSoup.
* It tries to extract the price and property title from specific HTML elements on the page.
* If the elements are not found, it sets these values to np.nan (a representation of "Not a Number" from the numpy library).
* The function returns a dictionary containing the property's price and name.
### 3. get_undervalued_properties(url) Function:

* This function takes a URL for a property listing page as input.
* It fetches the page content, parses it using BeautifulSoup, and finds all the property listings on the page.
* For each property listing, it extracts the URL of the property and uses the fetch_property_details function to retrieve detailed information, including price.
* The function attempts to convert the property price to a numeric value (float) and appends this information to a list of properties.
* If any errors occur during this process, it prints an error message and continues to the next property.
* The function returns a list of dictionaries, each representing a property with details such as URL, property details, and price.
### 4. Main Execution:

* The script defines the base URL for property listings and the total number of pages to scrape.
* It initializes an empty list, undervalued_properties, to store the details of undervalued properties.
* It iterates through the specified number of pages, calling the get_undervalued_properties function for each page and appending the results to the undervalued_properties list.
* After scraping the data, it creates a pandas DataFrame from the list of undervalued properties.
* Finally, it saves this DataFrame to a CSV file named 'undervalued_properties.csv'.
