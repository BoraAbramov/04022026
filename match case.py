
while True:
    _rating = int(input("Enter your rating: "))

    match _rating:
        case 1:
            _rating = "⭐"
        case 2:
            _rating = "⭐⭐"
        case 3:
            _rating = "⭐⭐⭐"
        case 4:
            _rating = "⭐⭐⭐⭐"
        case 5 :
            _rating = "⭐⭐⭐⭐⭐"
        case _:
            _rating = "not in range"
    print(_rating)


match _rating:
    case 1 | 2:  # יתפוס גם 1 וגם 2
        _rating = "Low rating"
    case 3:
        _rating = "Medium"
    case 4 | 5:  # יתפוס גם 4 וגם 5
        _rating = "High rating"

match _rating:
    case val if 1 <= val <= 3: # תופס את כל המספרים בין 1 ל-3
        _rating = "Low to Medium"
    case val if val > 3:      # תופס כל מספר שגדול מ-3
        _rating = "High"
    case _:
        _rating = "Not in range"

match True:
    case _ if _rating < 1:
        print("תוצאה: הדירוג נמוך מדי")

    case _ if 1 <= _rating <= 5:
        print(f"תוצאה: קיבלת {'⭐' * _rating}")

    case _ if _rating > 5:
        print("תוצאה: הדירוג גבוה מהטווח הסטנדרטי")

    case _:
        print("תוצאה: קלט לא תקין")