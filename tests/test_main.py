from src.main import add, square, add_10
# <python3 -m pytest test_main.py> in terminal to run the tests

def test_add():
    assert add(2, 3) == 5
    
def test_add_10():
    assert add_10(5) == 15
    
def test_square_4():
    assert square(4) == 16
    
def test_add_invalid():
    try:
        add(2, '3')
    except ValueError as e:
        assert str(e) == "Both arguments must be numbers."

def test_square_20():
    assert square(20) == 400