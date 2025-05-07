from selenium import webdriver
from selenium.webdriver.common.by import By
from schemas.looking_for import LookingFor

def srcrape_all_product_links_service(product: LookingFor) -> list:
    """
    Scrape OLX for a given product name and return the product details.
    """

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)

    try:
        search_query = product.name.replace(" ", "-")
        search_url = f"https://www.olx.ua/uk/list/q-{search_query}"
        driver.get(search_url)

        product_links = driver.find_elements(By.CSS_SELECTOR, "a.css-1tqlkj0")
        all_links = [link.get_attribute("href") for link in product_links]
        return all_links

    finally:
        driver.quit()
