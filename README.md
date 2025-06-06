# Python Job Scraper

This is a simple Python web scraping script that extracts Python-related job postings from [TimesJobs](https://www.timesjobs.com) using the `requests` and `BeautifulSoup` libraries.

## Features

- Scrapes job listings that match the keyword **"python"**
- Extracts:
  - Company Name
  - Required Skills
  - Published Date
- Filters and displays only jobs posted a **few days ago**

## Prerequisites

Make sure you have the following Python packages installed:

```bash
pip install requests beautifulsoup4 lxml
