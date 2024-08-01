import requests
from bs4 import BeautifulSoup
from datetime import date
from .models import JobTrend


def fetch_and_save_job_trends():
    url = "https://dev.bg"  # Replace with the target URL
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    data = parse_data(soup)

    today = date.today()
    for language, number_of_jobs in data.items():
        JobTrend.objects.update_or_create(
            programming_language=language,
            date=today,
            defaults={'number_of_jobs': number_of_jobs}
        )

    print(f"Data saved for {today}")

def parse_data(soup):
    # Initialize a dictionary to store job counts for the desired languages
    data = {
        "Python": 0,
        "Java": 0,
        "PHP": 0
    }

    # Find all relevant divs with the class "child-term"
    terms = soup.find_all("div", class_="child-term")
    for term in terms:
        language_element = term.find("a")
        if language_element:
            raw_string = language_element.get_text().strip()

            parts = raw_string.split()

            language_name = parts[0]
            number_of_jobs = parts[1]

            # Check if the language is one of the desired ones
            if language_name in data:
                data[language_name] = number_of_jobs

    return data