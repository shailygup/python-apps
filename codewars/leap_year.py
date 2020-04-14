# Author: @shailygupta
# leap_year


def leap_year(year):
    leap = False

    return (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0))


if __name__ == "__main__":
    # year = int(input())
    
    print(leap_year(1990))
    print(leap_year(2000))
    print(leap_year(2300))
    print(leap_year(1992))

    # Test Cases
    assert leap_year(1990) is False, "Should be False"
    assert leap_year(2000) is True, "Should be True"
    assert leap_year(2300) is False, "Should be False"
    assert leap_year(1992) is True, "Should be True"
