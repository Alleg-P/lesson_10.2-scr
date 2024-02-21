# Задача 2: Цвет фона для сайта

def get_background_color(current_hour):
    if current_hour >= 6 and current_hour < 18:
        return "Светлый"
    else:
        return "Темный"

current_hour = 10
background_color = get_background_color(current_hour)
print("Цвет фона:", background_color)

current_hour = 20
background_color = get_background_color(current_hour)
print("Цвет фона:", background_color)

current_hour = 5
background_color = get_background_color(current_hour)
print("Цвет фона:", background_color)
