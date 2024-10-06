def city_country(city, country):
    text = f'"{city.title()}, {country.title()}"'
    return text


test1  = city_country("Santiago", "Chile")
print(test1)
test2 = city_country("Sao Paulo", "brasil")
print(test2)
teste3 = city_country("salvador", "brasil")
print(teste3)