def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Неправильно введене ім'я користувача або номер"
        except KeyError:
            return "Користувача не найдено"
        except IndexError:
            return "Введіть імя користувача, якого телефон ви хочете дізнатись"


    return inner

