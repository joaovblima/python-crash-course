def build_profile(first_name, last_name, **user_info):
    user_info["firstname"] = first_name
    user_info["lastname"] = last_name
    return user_info

joao_profile = build_profile("joao", "lima",
                             age=27,
                             favorite_sport="jiujitsu")
print(joao_profile)