#Проверка длинны пароля
password = input('Введите пароль: ')
if len(password) < 8:
    print('Пароль слишком короткий!')

else:

    has_upper = any(el.isupper() for el in password)
    has_lower = any(el.islower() for el in password)
    has_digit = any(el.isdigit() for el in password)
    special_chars = '^%$#@-_=+?.<>'

    has_special = any(el in special_chars for el in password)

    if has_upper and has_lower and has_digit and has_special:
        print('✅ Пароль подходит!')

    else:
        print('⚠️  Пароль слабый!')
        if not has_upper:
            print('Добавьте заглавные буквы!(A-Z)')

        if not has_digit:
                print('Добавьте цифры в пароль!(0-9)')

        if not has_lower:
                print('Добавьте строчных букв в пароль!(a-z)')

        if not has_special:
                print('Спецсимволы - ^%$#@-_=+?.<>')
