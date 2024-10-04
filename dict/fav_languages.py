favorite_languages = {
    'joao': ['python', "java"],
    'maria': 'c',
    'leticia': ["rust", "go"],
    'ingrid': ['python'],
}

discord_friends = ["joao", "maria", "leticia", "ingrid", "maria alice", "gustavo"]

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages is:")
    for language in languages:
        print(f"{language.title()}")
    



