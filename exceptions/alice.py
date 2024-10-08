from pathlib import Path
path = Path("alice.txt")

def count_words(filename):
    try:
        contents = filename.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Desculpe, o arquivo {path} nao existe")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"o arquivo {path} tem {num_words} palavras")

    
filenames = ["alice.txt", "feiticeira,txt", "venderoa tigrinho.txt"]

for filename in filenames:
    path = Path(filename)   
    count_words(path)