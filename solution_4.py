# Задача 4: Выбор рекламной платформы

def choose_ad_platform(budget):
    if budget < 1000:
        return "Google"
    elif 1000 <= budget <= 5000:
        return "Facebook"
    else:
        return "Instagram"

budget = 500
ad_platform = choose_ad_platform(budget)
print(ad_platform)

budget = 3000
ad_platform = choose_ad_platform(budget)
print(ad_platform)

budget = 6000
ad_platform = choose_ad_platform(budget)
print(ad_platform)
