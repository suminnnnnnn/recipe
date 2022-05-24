from random import shuffle
from recipe2.models import recipe
from stockapp.models import Stock



# 재료 기반 레시피 추천
def recommend_ingredient(my_stock):
    all_recipes = recipe.objects.all()
    recommend_recipe_list = []
    this_stock = my_stock
    stock_list = []
    for stock in this_stock:
        stock_list.append(Stock.stock_stock)
        print(stock_list)
    for recipe in all_recipes:
        if not(recipe.ingredient):
            continue
        ss = recipe.ingredient.split(',')
        re_list = []
        for s in ss:
            re_list.append(int(s))

# 재고에 있는 재료를 모두 사용해서 만들 수 있는 요리부터 추천
        if len(re_list) != 0 and len(set(stock_list) - set(re_list)) == 0:
            if len(recommend_recipe_list) < 20:
                recommend_recipe_list.append(recipe.reci)
    if len(recommend_recipe_list) < 10:
        for recipe in all_recipes:
            if not (recipe.ingredient):
                continue
            ss = recipe.ingredient.split(',')
            re_list = []
            for s in ss:
                re_list.append(int(s))
            if len(re_list) != 0 and 0 < len(set(stock_list) - set(re_list)) < 2:  # and len(set(re_list) - set(stock_list)) < 10:
                if len(recommend_recipe_list) < 20:
                    recommend_recipe_list.append(recipe.reci)
    if len(recommend_recipe_list) < 10:
        for recipe in all_recipes:
            if not (recipe.ingredient):
                continue
            ss = recipe.ingredient_ids.split(',')
            re_list = []
            for s in ss:
                re_list.append(int(s))
            if len(re_list) != 0 and 1 < len(set(stock_list) - set(re_list)) < 3:
                if len(recommend_recipe_list) < 20:
                    recommend_recipe_list.append(recipe.reci)
    result = {}
    result['ids'] = recommend_recipe_list
    return result

#랜덤추천
def recommend_random():
    my_qset = recipe.objects.all()
    my_list = list(my_qset)
    shuffle(my_list)
    recommend_recipe_list = []
    for item in my_list[:20]:
        print(item.reci_id)
        recommend_recipe_list.append(item.reci_id)
    result = dict()
    result['ids'] = recommend_recipe_list
    return result