import random
import string
import time

# Simulate stock price data
def generate_stock_data(num_stocks=100):
    stocks = []
    for _ in range(num_stocks):
        symbol = ''.join(random.choices(string.ascii_uppercase, k=4))
        opening = round(random.uniform(10, 500), 2)
        closing = round(opening * random.uniform(0.95, 1.05), 2)
        stocks.append({'symbol': symbol, 'opening': opening, 'closing': closing})
    return stocks

# Calculate percentage change
def percentage_change(stock):
    return ((stock['closing'] - stock['opening']) / stock['opening']) * 100

# Heap Sort implementation
def heapify(arr, n, i, key):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and key(arr[l]) > key(arr[largest]):
        largest = l
    if r < n and key(arr[r]) > key(arr[largest]):
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, key)
    arr.reverse()  # To get descending order

# Search using Hash Map
def build_stock_map(stocks):
    return {stock['symbol']: stock for stock in stocks}

def search_stock(stock_map, symbol):
    return stock_map.get(symbol)

# Performance comparison
def performance_test():
    stocks = generate_stock_data(10000)
    stock_map = build_stock_map(stocks)
    symbols = [stock['symbol'] for stock in stocks]
    search_symbol = random.choice(symbols)

    # Heap Sort
    stocks_copy = stocks.copy()
    start = time.time()
    heap_sort(stocks_copy, key=percentage_change)
    heap_sort_time = time.time() - start

    # Standard sorted()
    start = time.time()
    sorted_stocks = sorted(stocks, key=percentage_change, reverse=True)
    sorted_time = time.time() - start

    # Hash Map search
    start = time.time()
    result = search_stock(stock_map, search_symbol)
    hash_search_time = time.time() - start

    # Standard list search
    start = time.time()
    result = next((stock for stock in stocks if stock['symbol'] == search_symbol), None)
    list_search_time = time.time() - start

    print(f"Heap Sort time: {heap_sort_time:.6f}s")
    print(f"sorted() time: {sorted_time:.6f}s")
    print(f"Hash Map search time: {hash_search_time:.6f}s")
    print(f"List search time: {list_search_time:.6f}s")
    print("Trade-offs:")
    print("- Heap Sort is efficient for large datasets but less convenient than sorted().")
    print("- Hash Map (dict) search is O(1) and much faster than list search (O(n)).")

if __name__ == "__main__":
    performance_test()