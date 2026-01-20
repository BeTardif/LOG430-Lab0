"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5
    assert my_calculator.addition(2,2) != 5

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(3, 2) == 1
    assert my_calculator.subtraction(4, 2) != 1

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(3, 2) == 6
    assert my_calculator.multiplication(4, 2) != 6

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(4, 2) == 2
    assert my_calculator.division(4, 2) != 3

#Failing test for Question 1
def test_failing():
    my_calculator = Calculator()
    #assert my_calculator.addition(2, 2) == 5

    #Oui, il mentionne la ligne dans le fichier test qui indique l'erreur dans les tests
    