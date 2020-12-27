def my_f(name, surname, date_of_birth, city, email, phone): #
    print('Проверьте данные пользователя: ',
          name, surname, date_of_birth, 'г.р.', city, email, phone,)
my_f(phone=(input('Введите номер телефона для связи: ')),
     name=(input('Введите Имя: ')),
     date_of_birth=(input('Введите дату рождения: ')),
     surname=(input('Введите Фамилию: ')),
     city=(input('Введите город пребывания: ')),
     email=(input('Введите email: ')))