import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

def scrape_books():
    """
    Scrape top 10 books from https://books.toscrape.com/
    and save the results to CSV file
    """
    # Target URL
    base_url = "https://books.toscrape.com/"
    
    # Headers to avoid blocking
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print("Fetching data from", base_url)
        
        # Request to main page
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()  # Will raise exception if status code is error
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all book articles
        book_articles = soup.find_all('article', class_='product_pod')
        
        if not book_articles:
            print("No book products found on this page")
            return
        
        # List to store book data
        books_data = []
        
        print(f"Found {len(book_articles)} books. Fetching top 10 books...")
        
        # Get top 10 books
        for i, article in enumerate(book_articles[:10]):
            try:
                # Extract book title
                title_element = article.find('h3').find('a')
                title = title_element.get('title') if title_element else "Title not found"
                
                # Extract price
                price_element = article.find('p', class_='price_color')
                price = price_element.text.strip() if price_element else "Price not found"
                
                # Extract availability
                availability_element = article.find('p', class_='instock availability')
                availability = availability_element.text.strip() if availability_element else "Status not found"
                
                # Extract product detail link
                link_element = article.find('h3').find('a')
                relative_url = link_element.get('href') if link_element else ""
                full_url = urljoin(base_url, relative_url) if relative_url else "URL not found"
                
                # Save book data
                book_data = {
                    'Title': title,
                    'Price': price,
                    'Availability': availability,
                    'URL': full_url
                }
                books_data.append(book_data)
                
                print(f"{i+1}. {title} - {price}")
                
                # Small delay to avoid rate limiting
                time.sleep(0.1)
                
            except Exception as e:
                print(f"Error processing book #{i+1}: {e}")
                continue
        
        # Save to CSV file
        if books_data:
            save_to_csv(books_data)
        else:
            print("No book data was successfully retrieved")
            
    except requests.RequestException as e:
        print(f"Error fetching data from website: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def save_to_csv(books_data):
    """
    Save book data to CSV file
    """
    filename = "books_data.csv"
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Define columns
            fieldnames = ['Title', 'Price', 'Availability', 'URL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write book data
            for book in books_data:
                writer.writerow(book)
        
        print(f"\nData successfully saved to file: {filename}")
        print(f"Total books saved: {len(books_data)}")
        
        # Show data preview
        print("\nPreview of saved data:")
        print("-" * 80)
        for i, book in enumerate(books_data[:3], 1):
            print(f"{i}. Title: {book['Title']}")
            print(f"   Price: {book['Price']}")
            print(f"   Status: {book['Availability']}")
            print(f"   URL: {book['URL']}")
            print("-" * 80)
        
        if len(books_data) > 3:
            print(f"... and {len(books_data) - 3} more books")
            
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    """
    Main function to run the scraper
    """
    print("=" * 60)
    print("WEB SCRAPER BOOKS.TOSCRAPE.COM")
    print("=" * 60)
    
    try:
        scrape_books()
    except KeyboardInterrupt:
        print("\nProcess stopped by user")
    except Exception as e:
        print(f"Error in main function: {e}")
    
    print("\nFinished!")

if __name__ == "__main__":
    main()
