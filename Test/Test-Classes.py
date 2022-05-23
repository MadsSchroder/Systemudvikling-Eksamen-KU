from Models.Classes import Classes

Hent_Undervisning = Classes("10, "Københavns Universitet", "08:00:00", "12:00:00", "Programmering")


def test_get_location():
    test = Hent_Undervisning.get_location() == "Københavns 89Universitet"
    assert test
    print(test)