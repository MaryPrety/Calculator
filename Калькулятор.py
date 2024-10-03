import math

# Память для хранения последних трех результатов
memory = [0, 0, 0]  

def update_memory(result):
    """Обновляет память, добавляя новый результат."""
    memory.pop(0)
    memory.append(result)

def get_number_from_input_or_memory():
    """Получает число от пользователя или использует результат из памяти."""
    choice = input("Введите число или 'm' для использования результата из памяти: ")
    if choice.lower() == 'm':
        print("Выберите результат из памяти:")
        for i, res in enumerate(memory, 1):
            print(f"{i}. {res}")
        mem_choice = int(input("Введите номер результата: "))
        if 1 <= mem_choice <= 3:
            return memory[mem_choice - 1]
        else:
            print("Неверный выбор.")
            return None
    else:
        try:
            return float(choice)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
            return None

def calculator():
    """Основная функция калькулятора."""
    print("Добро пожаловать в калькулятор!")
    
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Синус (sin)")
        print("6. Косинус (cos)")
        print("7. Тангенс (tan)")
        print("8. Квадратный корень (sqrt)")
        print("9. Возведение в степень (pow)")
        print("10. Натуральный логарифм (ln)")
        print("11. Десятичный логарифм (log10)")
        print("12. Экспонента (exp)")
        print("13. Выход")

        choice = input("Введите номер операции (1-13): ")

        if choice in ['1', '2', '3', '4']:
            num1 = get_number_from_input_or_memory()
            if num1 is None:
                continue
            num2 = get_number_from_input_or_memory()
            if num2 is None:
                continue

            if choice == '1':
                result = num1 + num2
                operation = "Сложение"
            elif choice == '2':
                result = num1 - num2
                operation = "Вычитание"
            elif choice == '3':
                result = num1 * num2
                operation = "Умножение"
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    operation = "Деление"
                else:
                    print("Ошибка! Деление на ноль невозможно.")
                    continue

            print(f"Результат ({operation}): {num1} {'+' if choice == '1' else '-' if choice == '2' else '*' if choice == '3' else '/'} {num2} = {result}")

        elif choice in ['5', '6', '7', '8', '9', '10', '11', '12']:
            num = get_number_from_input_or_memory()
            if num is None:
                continue

            if choice == '5':
                result = math.sin(math.radians(num))
                operation = "Синус"
            elif choice == '6':
                result = math.cos(math.radians(num))
                operation = "Косинус"
            elif choice == '7':
                result = math.tan(math.radians(num))
                operation = "Тангенс"
            elif choice == '8':
                if num >= 0:
                    result = math.sqrt(num)
                    operation = "Квадратный корень"
                else:
                    print("Ошибка! Квадратный корень из отрицательного числа невозможен.")
                    continue
            elif choice == '9':
                power = get_number_from_input_or_memory()
                if power is None:
                    continue
                result = math.pow(num, power)
                operation = "Возведение в степень"
            elif choice == '10':
                if num > 0:
                    result = math.log(num)
                    operation = "Натуральный логарифм"
                else:
                    print("Ошибка! Натуральный логарифм определен только для положительных чисел.")
                    continue
            elif choice == '11':
                if num > 0:
                    result = math.log10(num)
                    operation = "Десятичный логарифм"
                else:
                    print("Ошибка! Десятичный логарифм определен только для положительных чисел.")
                    continue
            elif choice == '12':
                result = math.exp(num)
                operation = "Экспонента"

            print(f"Результат ({operation}): {num} {'sin' if choice == '5' else 'cos' if choice == '6' else 'tan' if choice == '7' else ''} {result}")

        elif choice == '13':
            # Выход из программы
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите операцию от 1 до 13.")
            continue

        # Обновляем память с новым результатом
        update_memory(result)
        print(f"Текущая память: {memory}")

    print("Спасибо за использование калькулятора!")

if __name__ == "__main__":
    calculator()
