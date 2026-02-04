while True:
    _num2 = int(input("prime checker: "))
    _positive2 = _num2 > 1
    _remainder = 2
    if not _positive2 or _num2 == 0:
        continue
    if _num2 == 2:
        print("prime")
        continue
    while _remainder < _num2:
        _modulo = _num2 % _remainder == 0
        if _modulo:
            print("not a prime")
            break
        else:
            _remainder += 1
    if _modulo == False:
        print("prime")