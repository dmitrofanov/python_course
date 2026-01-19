purchases = [
    {"item": "яблоки", "category": "фрукты", "price": 150},
    {"item": "молоко", "category": "молочка", "price": 80},
    {"item": "хлеб", "category": "выпечка", "price": 60},
    {"item": "бананы", "category": "фрукты", "price": 120},
    {"item": "йогурт", "category": "молочка", "price": 45},
    {"item": "булка", "category": "выпечка", "price": 40}
]

# Каркас функции total_by_category:
def total_by_category(purchases_list):
    result = {}
    
    for purchase in purchases_list:  # purchase — это словарь
        category = purchase["________"]
        price = purchase["________"]
        
        if category in result:
            result[category] = result[category] + price
        else:
            result[category] = price
    
    return result
