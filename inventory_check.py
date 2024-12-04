def num_in_stock(fruit: str) -> int:
    """
    This function returns the number of a specific fruit Sophia has in stock.
    :param fruit: The name of the fruit.
    :return: The quantity of the fruit in stock, or 0 if not in stock.
    """
    inventory = {
        'apple': 2,
        'durian': 4,
        'pear': 1000
    }
    return inventory.get(fruit, 0)  

def main():
    fruit = input("Enter a fruit: ").strip().lower()  
    stock = num_in_stock(fruit)  
    
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == "__main__":
    main()