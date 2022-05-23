
# import requests
# from bs4 import BeautifulSoup

# foodlist = []
# number = 6979610
# while number > 6978610:
#     res = requests.get('https://www.10000recipe.com/recipe/'+str(number))
#     res = res.text
#     soup = BeautifulSoup(res)
#     food = []
#     for i in soup.select('div.view2_summary.st3>h3'):
#         food.append(i.text)
#     foodlist.append(food)
#     number -= 1

# print(foodlist) #레시피 리스트

# import re
# pat = re.compile('([ㄱ-힣]+)\d*')

# number = 6979610

# ingredient = []
# while number > 6978610:
#     res = requests.get('https://www.10000recipe.com/recipe/'+str(number))
#     res = res.text
#     soup = BeautifulSoup(res)
#     if soup is None:
#         ingredient.append(None)
#     else:
#         source = []
#         for i in soup.select('a > li'):
#             source.append( pat.findall(i.text)[0])
#         ingredient.append(source)
#     number -= 1


# print(ingredient) # 재료 리스트

# import urllib.request

# imglist = []
# number = 6979610
# while number > 6978610:
#     res = 'https://www.10000recipe.com/recipe/'+str(number)
#     req = urllib.request.Request(res)
#     res = urllib.request.urlopen(res).read()
#     soup = BeautifulSoup(res,'html.parser')
#     soup = soup.find("div",class_="centeredcrop")
#     if soup is None:
#         imglist.append(None)
#     else:
#         imgurl = soup.find("img")["src"]
#         imglist.append(imgurl)
#     number -= 1
    
# print(imglist) #음식사진 리스트


# import pandas as pd
    
# df = pd.DataFrame({ '레시피': foodlist,'재료' :ingredient, '음식사진':imglist})
    

# print(df)

# df.to_excel('C:/Users/admin/Desktop/recipe.xlsx', index=True)

