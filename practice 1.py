
while True:
    _rating = int(input("Enter a number between 1 and 5: "))
    _valid = 1 <= _rating <= 5
    if _valid:
        print("valid")
    else:
        print("invalid")
    _best = _rating == 5
    if _best:
        print("best")
    else:
        print("not best")
    _medium = 2 < _rating < 4
    if _valid and not _medium:
        print("score high or low")
    else:
        print("medium")

    _num = int(input("Enter a number: "))
    _positive = _num >= 0
    if _positive:
        print("positive")
    else:
        print("negative")
    _even = _num % 2 == 0
    if _even:
        print("even")
    else:
        print("odd")

    _num2 = int(input("prime checker: "))
    _positive2 = _num2 > 1
    _remainder = _num2
    _selfsplit = _num2 / _num2 == 1
    _modulo = _num2 % 2 != 0
    while _modulo != 0 and _remainder < _num2:
        if _positive2 and _selfsplit:
            print("prime")
        else:
            print("not prime")

