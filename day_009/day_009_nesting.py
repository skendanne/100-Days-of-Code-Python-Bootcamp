# Nesting lists and dictionaries:

# dictionary = {
#     "key1": "value",
#     "key2": [list],
#     "key3": {Dict},
#     }

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a Dictionary

# {
#     key: [list],
#     key2: Value
# }

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary into Dictionary

# {
#     key: {Dict},
#     key2 {Key: [List], Key2: {Dict}},
#     key3 [List],
# }

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visists": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visists": 5},
}

# Nesting Dictionary into a List

# [{
#     Key: [List],
#     Key2: {Dict},
# },
# {
#     Key: Value,
#     Key2, Value,
# }]

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visists": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visists": 5,
    },
]

# Exercise:

# You are going to write a program that adds to a travel_log. You can see
# a trave_log which is a list that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line
# 21 to add the entry for Russia to the travel_log

# add_new_country('Russia', 2, ["Moscow", "Saint Petersburg"])

# DO NOT modify the travel_log directly. You need to create a function
# that modifies it.

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    }
]

def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities,
    })

add_new_country('Russia', 2, ["Moscow", "Saint Petersburg"])
print(travel_log)