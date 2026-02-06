

while True:
    _time = input("enter valid time in minutes for cooking")
    if not _time.isdigit():
        print("please ", end="")
        continue
    else:
        _time = int(_time)
        while True:
            _price = input("enter valid price for meal")
            if  not _price.isdigit():
                print("please ", end="")
                continue
            else:
                _price = int(_price)
                break
    is_quick_service = _time < 15
    is_expensive = _price > 100
    if is_quick_service and not is_expensive:
        print("recommended")
    else:
        print("not recommended")

