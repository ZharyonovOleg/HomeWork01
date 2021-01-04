import sys
import time
if 'h' in sys.argv[1:]:
    print('Передайте данные для расчёта зарплаты сотрудника количество отработанных часов часовую ставку и размер премии через пробел')
else:

    hours, rate, bonus = sys.argv[1:]

    print(f'Расчёт зарплаты сотрудника: количество отработанных часов {hours} умножить на часовую ставку {rate} плюс премия {bonus}')
    time.sleep(4)
    total = int((int(hours) * int(rate)) + int(bonus))
    print(f'Что в итоге составило {total}')