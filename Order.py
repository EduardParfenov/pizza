# Заказ #

from Pizza import Pizza, PizzaBBQ, PizzaPepperoni, PizzaSeafood

import datetime

class Order:
    def __init__(self):
        self.amount = [] # список с заказанными пиццами
        self.len_kard = 52 # ширина вывода

    def add_datetime(self):
        return f'\nВремя заказа: {datetime.datetime.now()}'

    # def count_orders(self): # счетчик заказов
    #     self.number = 0
    #     count_orders = input('Хотите сделать Заказ? да/нет: ').lower().strip()
    #     while count_orders != 'нет':
    #         self.number += 1
    #         break
    #     return f'* {21} Заказ № {self.number} * {21}'

    def add_amount(self): # метод добавления пиц
        add_amount = input('\nДобавить пиццу в заказ? да/нет\n'
                           '->: ').lower().strip()
        while add_amount != 'нет':
            if add_amount == 'да':
                select = input('\nКакую пиццу желаете выбрать?\n'
                               '1. "Маргарита" \n'
                               '2. "Барбекю" \n'
                               '3. "Пепперони" \n'
                               '4. "Пицца с морепродуктами" \n'
                               '->: ')
                if select == '1':
                    pizza = Pizza()
                    pizza.add_filling()
                    pizza.del_filling()
                    pizza.get_info()
                    self.amount.append(pizza)
                elif select == '2':
                    pizza_bbq = PizzaBBQ()
                    pizza_bbq.add_filling()
                    pizza_bbq.del_filling()
                    pizza_bbq.get_info()
                    self.amount.append(pizza_bbq)
                elif select == '3':
                    pizza_pepperoni = PizzaPepperoni()
                    pizza_pepperoni.add_filling()
                    pizza_pepperoni.del_filling()
                    pizza_pepperoni.get_info()
                    self.amount.append(pizza_pepperoni)
                elif select == '4':
                    pizza_seafood = PizzaSeafood()
                    pizza_seafood.add_filling()
                    pizza_seafood.del_filling()
                    pizza_seafood.get_info()
                    self.amount.append(pizza_seafood)
                else:
                    print(f'Сделайте выбор согласно меню!')
            else:
                print('Выберите "да" или "нет"!')
            if add_amount == 'нет':
                break
            add_amount = input('\nХотите добавить пиццу в заказ? да/нет\n'
                               '->: ').lower().strip()

    def show_orders(self): # метод подсчета количества каждой заказанной пиццы и их стоимости
        print(f'\nКоличество заказанных пицц: {len(self.amount)} шт.\n')

        pizza_amount = dict()
        pizza_cost = dict()

        for num in range(len(self.amount)):
            pizza_name = self.amount[num].name  # переменная, которая принимает пиццы из списка self.amount по имени
            cost = self.amount[num].new_price   # переменная, которая принимает стоимость пиццы с допами

            if pizza_name in pizza_amount:
                pizza_amount[pizza_name] += 1
            else:
                pizza_amount[pizza_name] = 1

            if pizza_name in pizza_cost:
                pizza_cost[pizza_name] += cost
            else:
                pizza_cost[pizza_name] = cost

        for name1, count in pizza_amount.items():
            for name2, sum in pizza_cost.items():
                if name1 == name2:
                    print(f'| {name2} - {count} шт. на сумму: {sum} руб.')

        print(f'\nВремя заказа: {datetime.datetime.now()}')



x = Order()
# print(x.count_orders())
x.add_datetime()
x.add_amount()
x.show_orders()
