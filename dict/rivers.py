rivers = {
    "nilo": "egito", 
    "amazonas": "brasil",
    "mississipi": "eua",
}

for river, cities in rivers.items():
    print(f"O rio {river.title()} passa pelo {cities.title()}")