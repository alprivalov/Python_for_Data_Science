def NULL_not_found(object: any) -> int:
    if type(object) is float:
        print("Cheese:", object, type(object))

    elif type(object) is int and object == 0:
        print("Zero: ", object, type(object))

    elif type(object) is str:
        print("Empty: ", object, type(object))

    elif type(object) is bool:
        print("Fake: ", object, type(object))

    elif object is None:
        print("Nothing: ", object, type(object))

    else:
        print("Type not Found")
        return 1

    return 0
