register_url = 'https://stellarburgers.nomoreparties.site/register'  # адрес страницы регистрации
register_name_input_xpath = './/label[text()="Имя"]/parent::div/input'  # путь до элемента ввода имени
register_email_input_xpath = './/label[text()="Email"]/parent::div/input'  # путь до элемента ввода почты
register_password_input_xpath = './/label[text()="Пароль"]/parent::div/input'  # путь до элемента ввода пароля
register_button_xpath = './/button[text()="Зарегистрироваться"]'  # путь до кнопки регистрации
register_incorrect_password_text_xpath = './/label[text()="Пароль"]/parent::div/parent::div/p'  # путь до текста ошибки "Некорректный пароль"
register_password_div_xpath = './/label[text()="Пароль"]/parent::div'  # путь до блока ввода пароля
