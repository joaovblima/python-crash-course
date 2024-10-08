from pathlib import Path
path = Path("tropicana.txt")
content = "Da manga rosa eu quero o gosto e o sumo \n"
content += "Melao maduro sapoti, jua\n"
content += "Jaboticava teu olhar noturno\n"
content += "BEijo travoso de umbu-caja"
path.write_text(content)