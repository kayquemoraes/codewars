def cakes(recipe, available):
    cakes = []
    for ingredient, amount in recipe.items():
        if ingredient not in available:
            return 0
        cakes.append(available[ingredient] // amount)
    return min(cakes)