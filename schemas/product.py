from pydantic import BaseModel

class Product(BaseModel):
    """
    Product class to represent a product with its details.
    Attributes:
        name (str): The name of the product.
        description (str): A brief description of the product.
        price (float): The price of the product.
        phone (str): The phone number associated with the product.
    """

    name: str
    description: str
    price: float
    phone: str
