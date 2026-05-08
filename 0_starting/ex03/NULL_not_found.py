def NULL_not_found(object: any) -> int:
    if type(object) is type(None):
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float):
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object} {type(object)}")
    else:
        print("Type not found")
        return (1)
    return (0)
