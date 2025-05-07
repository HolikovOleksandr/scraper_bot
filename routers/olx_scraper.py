from fastapi import APIRouter
from schemas.looking_for import LookingFor
from services.srcrape_all_product_links_service import srcrape_all_product_links_service

router = APIRouter()


@router.post("/olx")
async def olx_scraper(product_name: LookingFor) -> list:
    """
    Scrape OLX for a given product name and return the product details.
    Parameters:
    - product_name: The name of the product to search for on OLX.
    Returns:
    - A list of product links found on OLX.
    """

    all_links = srcrape_all_product_links_service(product_name)

    products = [scrape_product(link) for link in all_links]
    return products