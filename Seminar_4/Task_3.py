# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Список для сохранения операций
operations = []

# Функция для отображения меню
def show_menu():
    print("\nВыберите операцию:")
    print("1. Проверить баланс")
    print("2. Внести деньги")
    print("3. Снять деньги")
    print("4. Показать историю операций")
    print("5. Выход")

# Функция для проверки баланса
def check_balance(balance):
    print(f"Ваш текущий баланс: {balance} руб.")

# Функция для внесения денег
def deposit(balance, amount):
    if amount <= 0:
        print("Сумма пополнения должна быть положительной!")
    else:
        balance += amount
        operations.append(f"Поступление: +{amount} руб.")
        print(f"Вы пополнили счет на {amount} руб.")
    return balance

# Функция для снятия денег
def withdraw(balance, amount):
    if amount <= 0:
        print("Сумма снятия должна быть положительной!")
    elif amount > balance:
        print("Недостаточно средств на счете!")
    else:
        balance -= amount
        operations.append(f"Снятие: -{amount} руб.")
        print(f"Вы сняли {amount} руб.")
    return balance

# Функция для отображения истории операций
def show_operations():
    if not operations:
        print("История операций пуста.")
    else:
        print("История операций:")
        for op in operations:
            print(op)

# Основная программа
def atm():
    balance = 0  # Начальный баланс
    while True:
        show_menu()
        choice = input("Введите номер операции: ")
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            try:
                amount = int(input("Введите сумму для пополнения: "))
                balance = deposit(balance, amount)
            except ValueError:
                print("Введите корректное число!")
        elif choice == "3":
            try:
                amount = int(input("Введите сумму для снятия: "))
                balance = withdraw(balance, amount)
            except ValueError:
                print("Введите корректное число!")
        elif choice == "4":
            show_operations()
        elif choice == "5":
            print("Спасибо за использование банкомата! До свидания.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
atm()
