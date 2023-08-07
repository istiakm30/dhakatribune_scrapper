
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def grabbing_info(limit):
    service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    categories = [
    'https://www.dhakatribune.com/bangladesh/politics',
    'https://www.dhakatribune.com/bangladesh/crime',
    'https://www.dhakatribune.com/bangladesh/education',
    'https://www.dhakatribune.com/business/economy',
    'https://www.dhakatribune.com/business/banks',
    'https://www.dhakatribune.com/business/commerce',
    'https://www.dhakatribune.com/business/stock',
    'https://www.dhakatribune.com/business/real-estate',
    'https://www.dhakatribune.com/sport/cricket',
    'https://www.dhakatribune.com/sport/football',
    'https://www.dhakatribune.com/sport/tennis',
    'https://www.dhakatribune.com/sport/other-sports',
    'https://www.dhakatribune.com/world/asia',
    'https://www.dhakatribune.com/world/south-asia',
    'https://www.dhakatribune.com/world/africa',
    'https://www.dhakatribune.com/world/middle-east',
    'https://www.dhakatribune.com/world/europe',
    'https://www.dhakatribune.com/world/north-america'
    ]

    for category in categories:
        print(f"Processing category: {category.split('/')[-1]}")
        links = getting_links(driver, category, limit)
        with open('scrapped_data/data.csv', 'a', encoding='utf-8') as f:
            for link in links:
                f.write(link.get_attribute('href') + ',' + category.split('/')[-1] + '\n')
    driver.quit()

def getting_links(driver, url, limit):
    driver.get(url)
    for i in range(limit):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            more_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='More'])[1]"))
            )
            more_button.click()
        except Exception as e:
            print(f"Error during scrolling or clicking More button: {e}")
            continue
    print("Attempting to fetch links...")
    links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "link_overlay")))
    print(f"Found {len(links)} links for category {url.split('/')[-1]}")
    return links
