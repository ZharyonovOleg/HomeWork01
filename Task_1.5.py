proceed = int(input('Введите сумму выручки в рублях: '))
cost = int(input('Введите сумму расходов в рублях: '))

if(proceed <= cost):
    print('Ваша Организация убыточна или сработала в ноль!')

if(proceed > cost):
    print('Ваша Организация прибыльна!')
    print('Рентабелность составила:', ((proceed - cost) / proceed) * 100, '%')
    numb_empl = int(input('Введите численность Организации: '))
    print('Прибыль, в расчёте на одного сотрудника, составила:', int((proceed - cost) / numb_empl), 'рублей')