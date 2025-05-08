from pydantic import BaseModel
from schemas.link import Link

class Product(BaseModel):
    """
    Product class to represent a product with its details.
    Attributes:
        name (str): The name of the product.
        description (str): A brief description of the product.
        price (float): The price of the product.
        phone (str): The phone number associated with the product.
        url (Link): The URL of the product page.
    """

    title: str
    description: str
    price: float
    phone: str
    url: Link
