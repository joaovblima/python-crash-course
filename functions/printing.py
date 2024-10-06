def printing_models(unprinted_disign, completed_models):

    while unprinted_disign:
        current = unprinted_disign.pop()
        print(f"Printing model: {current}")
        completed_models.append(current)


def show_completed_models(completed_models):
    for models in completed_models:
        print(f"Completed models: {models}")


unprinted_disign = ["phone case", "batman 3d", "duna action figure"]
complete = []

printing_models(unprinted_disign, complete)
show_completed_models(complete)