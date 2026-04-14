# Inventory system: Efficient search and sort algorithms for thousands of products

# Recommendation:
# - Search: Use a hash map (dictionary) for O(1) search by product ID, and an inverted index (dictionary) for O(1) search by name.
# - Sort: Use Timsort (Python's built-in sorted()), which is efficient for large datasets and stable.

# Justification:
# - Dataset size: Thousands of products (not millions), so in-memory structures are feasible.
# - Update frequency: Moderate; dictionaries allow fast updates.
# - Performance: Hash maps provide instant search; Timsort is optimal for real-world data.

# Implementation:

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price}, {self.quantity})"

class Inventory:
    def __init__(self):
        self.products = []
        self.id_index = {}
        self.name_index = {}

    def add_product(self, product):
        self.products.append(product)
        self.id_index[product.product_id] = product
        self.name_index[product.name.lower()] = product

    def search_by_id(self, product_id):
        return self.id_index.get(product_id)

    def search_by_name(self, name):
        return self.name_index.get(name.lower())

    def sort_by_price(self, reverse=False):
        return sorted(self.products, key=lambda p: p.price, reverse=reverse)

    def sort_by_quantity(self, reverse=False):
        return sorted(self.products, key=lambda p: p.quantity, reverse=reverse)

# Example usage:
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_product(Product("P001", "Apple", 1.2, 100))
    inventory.add_product(Product("P002", "Banana", 0.8, 150))
    inventory.add_product(Product("P003", "Orange", 1.5, 80))

    # Search
    print("Search by ID:", inventory.search_by_id("P002"))
    print("Search by Name:", inventory.search_by_name("orange"))

    # Sort
    print("Sort by Price:", inventory.sort_by_price())
    print("Sort by Quantity:", inventory.sort_by_quantity(reverse=True))
