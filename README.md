# Books.toscrape.com Web Scraper

A simple web scraper to fetch book data from [books.toscrape.com](https://books.toscrape.com/).

## Features

- Scrapes top 10 books from the main page
- Extracts information: Title, Price, Availability, and Detail URL
- Saves results to CSV file
- Robust error handling
- User-friendly output

## Dependencies

- `requests` - for HTTP requests
- `beautifulsoup4` - for HTML parsing
- `lxml` - fast parser for BeautifulSoup

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python book_scraper.py
```

2. The `books_data.csv` file will be created automatically with scraped data

## CSV Output

The CSV file will have the following columns:
- **Title**: Book title
- **Price**: Book price (in £XX.XX format)
- **Availability**: Stock status (In stock/Out of stock)
- **URL**: Link to product detail page

## Sample Output

```
Title,Price,Availability,URL
A Light in the Attic,£51.77,In stock,https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
Tipping the Velvet,£53.74,In stock,https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html
...
```

## Security Features

- User-Agent header to avoid blocking
- Rate limiting with request delays
- Timeout on HTTP requests
- Comprehensive error handling

## Notes

This script is created for educational purposes. Please ensure compliance with robots.txt and terms of service of the websites you scrape.
