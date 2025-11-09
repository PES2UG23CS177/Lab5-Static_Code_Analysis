import json
import logging
from datetime import datetime
import ast  # safer alternative to eval

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Global variable
stock_data = {}


def addItem(item="default", qty=0, logs=None):
    """Add items to stock safely with input validation."""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str):
        raise TypeError("Item name must be a string.")
    if not isinstance(qty, (int, float)):
        raise TypeError("Quantity must be a number.")

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info(f"Added {qty} of {item}. Current total: {stock_data[item]}")


def removeItem(item, qty):
    """Remove items from stock with proper error handling."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning(f"Tried to remove non-existent item: {item}")
    except Exception as e:
        logging.error(f"Error while removing item: {e}")


def getQty(item):
    """Get quantity of an item."""
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):
    """Load inventory data from file safely."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
            logging.info("Data loaded successfully.")
    except FileNotFoundError:
        logging.warning("File not found. Starting with empty inventory.")
    except json.JSONDecodeError:
        logging.error("Error decoding JSON data.")


def saveData(file="inventory.json"):
    """Save inventory data to file safely."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f)
            logging.info("Data saved successfully.")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")


def printData():
    """Print the full stock data."""
    print("Items Report:")
    for i, qty in stock_data.items():
        print(f"{i} -> {qty}")


def checkLowItems(threshold=5):
    """Return items below a given quantity threshold."""
    return [i for i, qty in stock_data.items() if qty < threshold]


def main():
    """Main program execution."""
    addItem("apple", 10)
    addItem("banana", -2)

    # Invalid types (will now raise controlled errors)
    try:
        addItem(123, "ten")
    except TypeError as e:
        logging.error(e)

    removeItem("apple", 3)
    removeItem("orange", 1)
    print(f"Apple stock: {getQty('apple')}")
    print(f"Low items: {checkLowItems()}")
    saveData()
    loadData()
    printData()

    # Replaced unsafe eval() with safe example
    ast.literal_eval("('Safe eval example', 42)")


if __name__ == "__main__":
    main()
