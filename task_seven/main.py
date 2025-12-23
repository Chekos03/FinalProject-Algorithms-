
def find_callories_greedy(products,budget):
    items = []
    for name, info in products.items():
        cost = info["cost"]
        calories = info["calories"]
        ratio = calories/cost
        items.append((name,cost,calories,ratio))
    items.sort(key=lambda x: x[3], reverse=True)

    selected = []
    total_calories = 0
    total_cost = 0
    for name, cost, calories, _ in items:
        if total_cost + cost <= budget:
            selected.append(name)
            total_cost += cost
            total_calories += calories

    return {"products": selected, 
            "total_calories": total_calories, 
            "total_cost": total_cost }




def find_min_callories(products,budget):
    items = []
    choice = [None] * (budget + 1)
    for name, info in products.items():
        cost = info["cost"]
        calories = info["calories"]
        items.append((name,cost,calories))

    dp = [0] * (budget + 1)

    for name,cost,calories in items:
        for b in range(budget,cost-1, -1):
            candidate = dp[b - cost] + calories
            if candidate > dp[b]:             
                dp[b] = candidate
                choice[b] = name

    selected = []
    total_cost = 0
    b = budget
    while b > 0 and choice[b] is not None:
        name = choice[b]
        selected.append(name)
        c = products[name]["cost"]
        total_cost += c
        b -= c

    selected.reverse()

    return {
        "products": selected,
        "total_calories": dp[budget],
        "total_cost":total_cost
    }

budget = 100
products = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

result_greedy = find_callories_greedy(products,budget)
print(f'Результат виконання жадібного алгоритму :{result_greedy}')
result_dp= find_min_callories(products,budget)
print(f'Результат виконання dp :{result_dp}')






