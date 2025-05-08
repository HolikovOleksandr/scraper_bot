from schemas.link import Link
from selenium import webdriver
from selenium.webdriver.common.by import By
from schemas.product import Product



def scrape_product(link: Link) -> dict:
    """
    Scrape product details from a given link.
    Parameters:
    - link: The URL of the product page to scrape.
    Returns:
    - A dictionary containing the scraped product details.
    """

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(link)
        driver.implicitly_wait(2)  

        # show_phone_button = driver.find_element(By.CSS_SELECTOR, ".css-118x51")
        # show_phone_button.click()
        
        title = driver.find_elements(By.CSS_SELECTOR, "h4")[0].text
        print(title)
        # description = driver.find_element(By.CLASS_NAME, ".css-19duwlz").text
        # price=float(driver.find_element(By.CLASS_NAME,"css-fqcbii").text)
        # phone = driver.find_element(By.CSS_SELECTOR, ".css-v1ndtc").text.split()
        # url = driver.current_url

        return {
            "title": title,
            # "price": price,
            # "description": description,
            # "phone": phone,
            # "url": url
        }
    
        # return dict(Product(title, price, description, phone, url))

    except Exception as e:
        print(f"An error occurred while scraping the product: {e}")
        return None
    
    finally:
        driver.quit()
