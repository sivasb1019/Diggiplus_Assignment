# Web Scraping to analyse projects in Upwork, filter them and get the list of best ones.

### 1. Importing Libraries:

* The code starts by importing the necessary Python libraries: requests for making HTTP requests, BeautifulSoup from the bs4 library for web scraping, and pandas for data manipulation.
### 2. scrape_upwork_jobs Function:

* This is the main function that performs the scraping and filtering of Upwork job listings. It takes two arguments: search_query and min_budget.
* It constructs the base URL for the Upwork job search using the search_query.
* It initializes the page_number to 1 and creates an empty list called jobs to store the job data.
### 3. Web Scraping Loop:
 
* The code enters a while True loop to iterate through the pages of job listings on Upwork.
* It constructs the URL for the current page by appending the page_number to the base URL.
* It makes an HTTP GET request to the URL and parses the HTML content using BeautifulSoup.
### 4. Extracting Job Listings:

* It uses BeautifulSoup to find all job listings on the page with the class 'up-card-section pt-0'.
* It prints the job_listings to the console for debugging.
### 5. Checking for End of Listings:

* If there are no job listings (job_listings is empty), it breaks out of the loop as it indicates the end of the listings.
### Iterating Through Job Listings:

* It iterates through each job listing in job_listings.
### 6. Extracting Job Information:

* It extracts job information, including the title, description, and budget from each job listing.
* It checks for hourly rate jobs and skips them.
* It removes dollar signs and commas from the budget and converts it to an integer.
* It checks if the job's budget is below the specified minimum budget and skips it if it is.
### 7. Storing Job Data:

* If a job passes all the filters, it creates a dictionary containing the job's title, description, and budget and appends it to the jobs list.
### 8. Incrementing page_number:

* After processing all job listings on the current page, it increments the page_number to move to the next page.
### 9. Returning the jobs List:

* Once all pages have been scraped and filtered, the function returns the jobs list containing the filtered job data.
### 10. Main Block:

* The script checks if it's being run as the main program using if __name__ == "__main__":.
* It calls the scrape_upwork_jobs function with the search query "python" and a minimum budget of 45.
* If job listings are found, it creates a DataFrame using pandas and prints it. Otherwise, it prints "No matching jobs found."
