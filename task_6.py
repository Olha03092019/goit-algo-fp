
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Greedy approach
def greedy_algorithm(items, budget):
    # формуємо список страв із співвідношенням калорій до вартості
    items_with_ratio = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        items_with_ratio.append((name, info["cost"], info["calories"], ratio))

    # сортуємо страви за спаданням співвідношення калорій до вартості
    items_with_ratio.sort(key=lambda x: x[3], reverse=True)

    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    # послідовно додаємо страви, поки вистачає бюджету
    for name, cost, calories, ratio in items_with_ratio:
        if cost <= remaining_budget:
            remaining_budget -= cost
            total_calories+= calories
            chosen_items.append(name)

    # повертаємо калорійність, витрачений бюджет та список обраних страв
    return total_calories, budget - remaining_budget, chosen_items


# Dynamic Programming approach
def dynamic_programming(items, budget):
    # список назв усіх доступних страв
    item_names = list(items.keys())

    dp_table = [0] * (budget + 1)
    chosen = [set() for _ in range(budget + 1)]

    # для кожної страви оновлюємо dp-таблицю
    for item in item_names:
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        # проходимо бюджет у зворотному порядку,
        # щоб кожну страву можна було використати лише один раз
        for b in range(budget, cost - 1, -1):
           if dp_table[b-cost]+calories > dp_table[b]:
               dp_table[b] = dp_table[b-cost] + calories
               chosen[b] = chosen[b-cost].copy()
               chosen[b].add(item)

    # фінальний результат для повного бюджету
    total_calories = dp_table[budget]
    chosen_items = list(chosen[budget])
    total_cost = sum(items[item]["cost"] for item in chosen_items)

    return total_calories, total_cost, chosen_items

if __name__ == '__main__':
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(f"\nGreedy approach: {greedy_result}, "
          f"\nDynamic Programming approach: {dp_result}")
