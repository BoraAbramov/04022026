
while True:
    _volume = int(input("select volume between 1 and 10"))
    if _volume > 10 or _volume < 1:
        print("please try again and", end=" ")
    else:
        match _volume:
            case 1:
                _volume = "very quiet"
            case 2:
                _volume = "quiet"
            case 3:
                _volume = "low"
            case 4:
                _volume = "low"
            case 5:
                _volume = "medium"
            case 6:
                _volume = "medium high"
            case 7:
                _volume = "loud"
            case 8:
                _volume = "very loud"
            case 9 | 10:
                _volume = "max volume"
        print(_volume)