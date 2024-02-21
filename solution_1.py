# Задача 1: Скидки в магазине Романа

def calculate_final_cost(initial_cost, visits):
    discount = 0
    if visits >= 20:
        discount = 0.2
    elif visits >= 10:
        discount = 0.1

    final_cost = initial_cost - (initial_cost * discount)
    return int(final_cost)

initial_cost = 100
visits = 5
final_cost = calculate_final_cost(initial_cost, visits)
print("Итоговая стоимость:", final_cost)

initial_cost = 200
visits = 10
final_cost = calculate_final_cost(initial_cost, visits)
print("Итоговая стоимость:", final_cost)

initial_cost = 150
visits = 20
final_cost = calculate_final_cost(initial_cost, visits)
print("Итоговая стоимость:", final_cost)
