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

    try:
        # Initialize the Selenium WebDriver
        driver = webdriver.Chrome()
        driver.get(link)

        # Wait for the page to load
        driver.implicitly_wait(2)  

        # Clicking a button to show the phone number
        show_phone_button = driver.find_element(By.CSS_SELECTOR, ".css-118x51")
        show_phone_button.click()
        
        # Example of scraping product details
        title = driver.find_element(By.CLASS_NAME, "css-10ofhqw").text
        description = driver.find_element(By.CLASS_NAME, ".css-19duwlz").text
        price=float(driver.find_element(By.CLASS_NAME,"css-fqcbii").text)
        phone = driver.find_element(By.CSS_SELECTOR, ".css-v1ndtc").text.split()
        url = driver.current_url

        return Product(title, price, description, phone, url)

    except Exception as e:
        print(f"An error occurred while scraping the product: {e}")
        return None
    
    finally:
        driver.quit()
