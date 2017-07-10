# Ближайшие бары

Консольный скрипт, который рассчитает:

- самый большой бар;
- самый маленький бар;
- самый близкий бар (текущие десятичные gps-координаты
ввести с клавиатуры).

из .json такого фотмата:
```json
[
   {
        "global_id": 281494747,
        "SeatsCount": 10,
        "Latitude_WGS84": "55.6957036590694730",
        "Longitude_WGS84": "37.4983186013284640",
        "geoData": {
            "coordinates": [
                37.49831860129411,
                55.695703659188716
            ],
            "type": "Point"
        },
        "Address": "Мичуринский проспект, дом 31, корпус 7",
        "ID": "00145556",
        "TypeObject": "бар",
        "IsNetObject": "нет",
        "Name": "БАР",
        "system_object_id": "00145556",
        "PublicPhone": [
            {
                "PublicPhone": "нет телефона",
                "global_object_id": 281494747.0,
                "global_id": 35021.0,
                "system_object_id": "00145556 _1"
            }
        ],
        "AdmArea": "Западный административный округ",
        "SocialPrivileges": "нет",
        "District": "район Раменки"
    },
    ...
]
```
Данные по барам Москвы можно скачать здесь
http://data.mos.ru/opendata/7710881420-bary в секции скачать.
Скрипт не берет в рассчет бары с колличеством мест меньше 5

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux, Mac OSX:

```#!bash

$ python bars.py <filename> # possibly requires call of python3 executive instead of just python

$ python3 bars.py 'data-2897-2016-11-23.json'

Biggest bar is: Спорт бар «Красная машина»
Smallest bar is: Бар «Витамин»
Input GPS coordinates in format Latitude, Longitude :
>>> 55.78499, 37.464747
Closest bar is: Грэйс Бар

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
