from sss import validate_credentials


def test_password_exact_8_chars():
    assert validate_credentials('user123', '12345678') is True


def test_password_less_than_8_chars():
    assert validate_credentials('user123', '1234567') is False


def test_password_more_than_8_chars():
    assert validate_credentials('user123', '1234567890') is True


def test_empty_login():
    assert validate_credentials('', '12345678') is False


def test_empty_password():
    assert validate_credentials('user123', '') is False


def test_whitespace_only_login():
    assert validate_credentials('   ', '12345678') is False

print('Все тесты прошли успешно!')
