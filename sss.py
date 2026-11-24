def validate_credentials(login: str, password: str) -> bool:
    if not isinstance(login, str) or not isinstance(password, str):
        return False

    if not login.strip():
        return False

    if len(password) < 8:
        return False

    return True


if __name__ == '__main__':
    user_login = input('Введите логин: ')
    user_password = input('Введите пароль: ')
    print('Результат проверки:', validate_credentials(user_login, user_password))
