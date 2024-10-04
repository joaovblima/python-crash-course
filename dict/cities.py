cities = {
    "sao paulo": {
        "pais": "brasil",
        "populacao": 11451245,
        "fato": "maior metropole",
    }, 
    "rio de janeiro": {
        "pais": "brasil",
        "populacao": 16054524,
        "fato": "cidade mais quente do Brasil",
    },
    "uniao dos palmares":{
        "pais": "brasil",
        "populacao": 65000,
        "fato": "terra de zumbi",
    },
}


for city, city_info in cities.items():
    print(f"{city.title()}:")
    print(f"\tPais: {city_info["pais"].title()}")
    print(f"\tPopulacao: {city_info["populacao"]}")
    print(f"\tFato: {city_info["fato"].title()}")
    print()