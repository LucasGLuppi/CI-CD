def suma(a, b):
    return a + b


def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def resta(a, b):
    return a - b

def test_resta():
    assert resta(2, 5) == -3
    assert resta(4, 1) == 3
    
def multiplicacion(a, b):
    return a * b

def test_multiplicacion():
    assert multiplicacion(2, 5) == 10
    assert multiplicacion(3, 11) == 33