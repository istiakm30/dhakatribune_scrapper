
# Dhaka Tribune Web Scraper

This set of scripts provides functionality to scrape content from various categories of the [Dhaka Tribune](https://www.dhakatribune.com/) website. It collects URLs from the selected categories and subsequently extracts the title and body content from each URL.

---

## File Descriptions:

1. **main.py**:
    - Main script to initiate the scraping process.
    - Prompts the user to enter the number of pages to scrape.
    - Handles URL grabbing and content scraping through auxiliary scripts.
    
2. **url_grabber.py**:
    - Utilizes Selenium to navigate the Dhaka Tribune website.
    - Collects URLs from various categories based on user input.
    
3. **scraper.py**:
    - Uses `requests` and `BeautifulSoup` to scrape content from the provided URLs.
    - Extracts title and body of the articles.
    - Saves the scraped data into category-specific CSV files.
    - Provides backup functionality for previous data.

---

## Usage:

1. Ensure all dependencies are installed:
    ```bash
    pip install requests beautifulsoup4 selenium pandas tqdm webdriver_manager
    ```

2. Run the `main.py` script:
    ```bash
    python main.py
    ```

3. Follow the on-screen prompts to specify the number of pages you want to scrape.

4. After completion, check the `scrapped_data` directory for the saved CSV files.

---

## Dependencies:

- requests
- beautifulsoup4
- selenium
- pandas
- tqdm
- webdriver_manager

---

## Disclaimer:

Do not use it more than once withing a half hour period avoid overloading the server with frequent requests.

---
