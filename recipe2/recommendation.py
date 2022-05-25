from random import shuffle
from recipe2.models import recipe
from stockapp.models import Stock

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