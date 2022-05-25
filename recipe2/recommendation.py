from random import shuffle
from recipe2.models import recipe
from stockapp.models import Stock

#사용자 재고 기반 추천
#사용자 재고 리스트 가져오기

# def get_stock_list():
#      all_stock = Stock.objects.filter(stock_user=request.user)
#      stock_list = []
#      for stock in all_stock:
#          stock_list.append(stock.stock_stock)
#     return stock_list 


# def get_recipe_list():
#     all_recipe = recipe.objebts.all()
#     recommend_recipe_list = []
#     for recipe in all_recipe:
#         recommend_recipe_list.append(recipe.recipe)
#     return recommend_recipe_list


#랜덤추천
def recommend_random():
    my_qset = recipe.objects.all()
    my_list = list(my_qset)
    shuffle(my_list)
    recommend_recipe_id_list = []
    for item in my_list[:20]:
        print(item.recipe)
        recommend_recipe_id_list.append(item.recipe)
    result = dict()
    result['ids'] = recommend_recipe_id_list
    return result