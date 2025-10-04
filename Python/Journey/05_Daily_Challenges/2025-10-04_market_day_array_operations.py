# -----------------------------------------------------------------------------
# File: market_operations.py
# Author: Your Name
# Description:
#     Implements a function to manage an array of product dictionaries in a 
#     market setting. Supports adding new products, removing products, and 
#     updating product prices. Ensures correct handling of existing products.
# -----------------------------------------------------------------------------

def market_operations(products, operation, product_info):
    """
    Manage an array of products with add, remove, and update_price operations.

    Parameters:
    -----------
    products : list of dict
        A list of product dictionaries. Each product has:
            - 'name' (str)
            - 'quantity' (int)
            - 'price_per_unit' (float)
    operation : str
        Operation to perform. Options:
            - 'add': Add a new product or increase quantity of existing product.
            - 'remove': Remove a product by name.
            - 'update_price': Update price per unit of an existing product.
    product_info : dict
        Dictionary containing product info relevant to the operation:
            - For 'add': requires 'name', 'quantity', 'price_per_unit'.
            - For 'remove': requires 'name'.
            - For 'update_price': requires 'name', 'price_per_unit'.

    Returns:
    --------
    list of dict
        Updated list of products after performing the operation.
    """

    if operation == "add":
        # Check if product already exists
        for product in products:
            if product["name"] == product_info["name"]:
                # If exists, increment quantity and update price
                product["quantity"] += product_info["quantity"]
                product["price_per_unit"] = product_info["price_per_unit"]
                break
        else:
            # If product does not exist, append new product
            products.append(product_info)

    elif operation == "remove":
        # Remove all products with matching name
        products = [product for product in products if product["name"] != product_info["name"]]

    elif operation == "update_price":
        # Update price for the product with matching name
        for product in products:
            if product["name"] == product_info["name"]:
                product["price_per_unit"] = product_info["price_per_unit"]
                break

    return products


# -----------------------------------------------------------------------------
# Example Usage / Test Cases
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    products = []

    # Add a product
    print(market_operations(products, "add", {"name": "Apples", "quantity": 10, "price_per_unit": 0.5}))
    # [{'name': 'Apples', 'quantity': 10, 'price_per_unit': 0.5}]

    # Add another product
    print(market_operations(products, "add", {"name": "Bananas", "quantity": 5, "price_per_unit": 1.0}))
    # [{'name': 'Apples', 'quantity': 10, 'price_per_unit': 0.5}, {'name': 'Bananas', 'quantity': 5, 'price_per_unit': 1.0}]

    # Update existing product (quantity + price)
    print(market_operations(products, "add", {"name": "Apples", "quantity": 5, "price_per_unit": 0.75}))
    # [{'name': 'Apples', 'quantity': 15, 'price_per_unit': 0.75}, {'name': 'Bananas', 'quantity': 5, 'price_per_unit': 1.0}]

    # Update price
    print(market_operations(products, "update_price", {"name": "Bananas", "price_per_unit": 1.2}))
    # [{'name': 'Apples', 'quantity': 15, 'price_per_unit': 0.75}, {'name': 'Bananas', 'quantity': 5, 'price_per_unit': 1.2}]

    # Remove product
    print(market_operations(products, "remove", {"name": "Apples"}))
    # [{'name': 'Bananas', 'quantity': 5, 'price_per_unit': 1.2}]
