# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

from itertools import combinations

def find_one_variant(items, max_weight):
    """Возвращает один допустимый вариант комплектации рюкзака."""
    current_weight = 0
    backpack = []
    
    for item, weight in items.items():
        if current_weight + weight <= max_weight:
            backpack.append(item)
            current_weight += weight
    
    return backpack, current_weight

def find_all_variants(items, max_weight):
    """Возвращает все возможные варианты комплектации рюкзака."""
    all_variants = []
    item_list = list(items.items())
    
    for r in range(1, len(item_list) + 1):
        for combination in combinations(item_list, r):
            total_weight = sum(weight for _, weight in combination)
            if total_weight <= max_weight:
                all_variants.append([item for item, _ in combination])
    
    return all_variants

# Словарь с вещами и их массой
items = {
    "палатка": 5,
    "спальный мешок": 2,
    "еда": 4,
    "вода": 3,
    "фонарик": 1,
    "аптечка": 1,
    "нож": 1,
    "карта": 1,
    "теплая одежда": 4,
}

# Максимальная грузоподъёмность рюкзака
max_weight = 10

# Один допустимый вариант
one_variant, total_weight = find_one_variant(items, max_weight)
print(f"Один вариант: {one_variant}, вес: {total_weight} кг")

# Все возможные варианты
all_variants = find_all_variants(items, max_weight)
print("\nВсе возможные варианты:")
for variant in all_variants:
    print(variant)
