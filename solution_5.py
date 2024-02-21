# Задача 5: Комплексный анализ эффективности рекламы

def analyze_ad_efficiency(clicks, impressions, views):
    click_to_impression_ratio = clicks / impressions

    if click_to_impression_ratio < 0.01 and views >= impressions:
        return "Недооцененная"
    elif 0.01 <= click_to_impression_ratio < 0.05:
        return "Низкая"
    elif 0.05 < click_to_impression_ratio <= 0.1 and views > clicks:
        return "Средняя"
    elif click_to_impression_ratio > 0.1:
        return "Высокая"
    else:
        return "Неопределенная"

clicks = 50
impressions = 10000
views = 15000
ad_efficiency = analyze_ad_efficiency(clicks, impressions, views)
print("Оценка эффективности рекламы:", ad_efficiency)

clicks = 200
impressions = 10000
views = 5000
ad_efficiency = analyze_ad_efficiency(clicks, impressions, views)
print("Оценка эффективности рекламы:", ad_efficiency)

clicks = 700
impressions = 10000
views = 800
ad_efficiency = analyze_ad_efficiency(clicks, impressions, views)
print("Оценка эффективности рекламы:", ad_efficiency)

clicks = 1200
impressions = 10000
views = 1000
ad_efficiency = analyze_ad_efficiency(clicks, impressions, views)
print("Оценка эффективности рекламы:", ad_efficiency)

clicks = 500
impressions = 10000
views = 200
ad_efficiency = analyze_ad_efficiency(clicks, impressions, views)
print("Оценка эффективности рекламы:", ad_efficiency)
