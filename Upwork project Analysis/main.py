import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_upwork_jobs(search_query, min_budget):
    base_url = f"https://www.upwork.com/search/jobs/?q={search_query}"
    page_number = 1
    jobs = []

    while True:
        url = f"{base_url}&page={page_number}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        job_listings = soup.find_all('div', class_='up-card-section pt-0')
        print(job_listings)

        if not job_listings:
            break

        for job_listing in job_listings:
            title_element = soup.find('a', {'class': 'up-n-link'})
            title = title_element.text.strip() if title_element else 'Not Found'
            description_element = soup.find('span', {'class': 'job-description-text'})
            description = description_element.text.strip() if description_element else 'Not Found'
            budget_element = soup.find('small', {'class': "text-muted display-inline-block-text-muted"})
            print(budget_element)
            budget = budget_element.text.split()[-1].strip() if budget_element else 'Not Found'
            print(budget)
            '''title = soup.find('a', class_='up-n-link').text.strip()
            description = soup.find('span', class_='job-description-text').text.strip()
            budget = soup.find('strong', class_='js-budget').text.strip()'''

            # Filter by minimum budget
            if 'hour' in budget:
                continue  # Skip hourly rate jobs
            budget = budget.replace("$", "").replace(",", "")
            if int(budget) < min_budget:
                continue  # Skip jobs with budgets below the minimum

            job = {
                'Title': title,
                'Description': description,
                'Budget': budget,
            }
            jobs.append(job)

        page_number += 1

    return jobs

if __name__ == "__main__":
    '''search_query = input("Job Title: ")  # Customize your search query
    min_budget = int(input("Minimum Budget: "))  # Customize your minimum budget'''

    job_list = scrape_upwork_jobs("python", 45)

    if job_list:
        df = pd.DataFrame(job_list)
        print(df)
    else:
        print("No matching jobs found.")
