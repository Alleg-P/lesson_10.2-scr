# Задача 7: Расчет скидок

def calculate_discount(prices, index=0, discount = 0):
    if index == len(prices):
        return prices
    new_price = prices[index] - discount
    discount = prices[index] * 0.1
    prices[index] = int(new_price)
    return calculate_discount(prices, index+1, discount)

prices = [1000, 2000, 3000, 5000, 10000, 15000]
discount_prices = calculate_discount(prices)
discount_prices_str = ', '.join(map(str, discount_prices))
print("Выходные данные:", discount_prices_str)

prices = [100, 200, 300, 400]
discount_prices = calculate_discount(prices)
discount_prices_str = ', '.join(map(str, discount_prices))
print("Выходные данные:", discount_prices_str)

prices = [50, 100]
discount_prices = calculate_discount(prices)
discount_prices_str = ', '.join(map(str, discount_prices))
print("Выходные данные:", discount_prices_str)
