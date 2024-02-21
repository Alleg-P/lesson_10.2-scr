# Задача 6: Поиск максимального элемента

def find_max_price(prices):
    if len(prices) == 1:
        return prices[0]
    else:
        max_price = find_max_price(prices[1:])
        if prices[0] > max_price:
            return prices[0]
        else:
            return max_price

prices = [15, 7, 9]
max_price = find_max_price(prices)
print(max_price)

prices = [1, 10, 20, 5]
max_price = find_max_price(prices)
print(max_price)

prices = [25, 25, 25]
max_price = find_max_price(prices)
print(max_price)

prices = [10, 8, 12]
max_price = find_max_price(prices)
print(max_price)
