import url_grabber
import scraper

def main():
    tried = 0
    while tried < 3:
        user_input = input("Enter the number of pages you want to scrape: ")
        try:
            # Grabbing URLs
            print("Grabbing URLs...")
            url_grabber.grabbing_info(int(user_input))
            
            # Scraping content from the URLs
            print("Scraping data from the URLs...")
            scraper.scraper_code_with_no_headers()
            break
        except ValueError as e:
            print(f"Error occurred: {str(e)}")
            tried += 1
            if tried == 3:
                print("You have exceeded the maximum number of tries. Please try again later.")
                exit()

if __name__ == "__main__":
    main()
