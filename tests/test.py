import string
from password.new_password import generate_password

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    for length in range(1, 21):
        assert len(generate_password(length)) == length

def test_password_randomness():
    """Тест, что два сгенерированных пароля различаются"""
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2 
