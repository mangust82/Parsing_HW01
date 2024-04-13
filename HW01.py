# Ознакомиться с некоторые интересными API. https://docs.ozon.ru/api/seller/ https://developers.google.com/youtube/v3/getting-started https://spoonacular.com/food-api
# Потренируйтесь делать запросы к API. Выберите публичный API, который вас интересует, и потренируйтесь делать API-запросы с помощью Postman. Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.
# Сценарий Foursquare
# Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
# Используйте API Foursquare для поиска заведений в указанной категории.
# Получите название заведения, его адрес и рейтинг для каждого из них.
# Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

import requests
import json
import pandas as pd
import csv

url = "https://api.foursquare.com/v3/places/search"

client_id = "__"
client_secret = "__"

city = input('Enter the city: ')
category = input('Enter the catagory: ')

# city = 'москва'
# category = 'бассейн'

params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'near': city,
        'query': category
}

headers = { "Accept": "application/json",
            "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="}


response = requests.get(url, params=params, headers=headers)
if response.status_code ==200:
    dict_category = json.loads(response.text)
else:
    print(f'ошибка запроса {response.status_code}')

# with open('my_category.json', "w+", encoding='UTF-8') as f:
#     print(f.write(response.text))
    

df_list = []
for categ in dict_category['results']:
    cat_dict = {}
    cat_dict['name'] = categ['name']
    try:
        cat_dict['address'] = categ['location']['address']
    except KeyError:
        cat_dict['address'] = 'No adress'
    try:
        cat_dict['city'] = categ['location']['locality']
    except KeyError:
        cat_dict['city'] = 'No city'
    try:
        cat_dict['широта'] = categ['geocodes']['main']['latitude']
    except KeyError:
        cat_dict['широта'] = 'no'
    try:
        cat_dict['долгота'] = categ['geocodes']['main']['longitude']
    except KeyError:
        cat_dict['долгота'] = 'no'
    
    df_list.append(cat_dict)

df = pd.DataFrame(df_list)
print(df.head(100))

reply_str = json.dumps(df_list)
with open('reply.json', "w+", encoding='UTF-8') as f:
    f.write(reply_str)
